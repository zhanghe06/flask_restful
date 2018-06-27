# MariaDB


## MySQL 事务

一般来说，事务是必须满足4个条件（ACID）：
1. 原子性（Atomicity，或称不可分割性）
2. 一致性（Consistency）
3. 隔离性（Isolation，又称独立性）
4. 持久性（Durability）

- 原子性：一个事务（transaction）中的所有操作，要么全部完成，要么全部不完成，不会结束在中间某个环节。事务在执行过程中发生错误，会被回滚（Rollback）到事务开始前的状态，就像这个事务从来没有执行过一样。

- 一致性：在事务开始之前和事务结束以后，数据库的完整性没有被破坏。这表示写入的资料必须完全符合所有的预设规则，这包含资料的精确度、串联性以及后续数据库可以自发性地完成预定的工作。

- 隔离性：数据库允许多个并发事务同时对其数据进行读写和修改的能力，隔离性可以防止多个事务并发执行时由于交叉执行而导致数据的不一致。事务隔离分为不同级别，包括读未提交（Read uncommitted）、读提交（read committed）、可重复读（repeatable read）和串行化（Serializable）。

- 持久性：事务处理结束后，对数据的修改就是永久的，即便系统故障也不会丢失。


## 测试 “幻读”（phantom read）

因高并发场景下, 会出现同一时刻交叉多个事务的情况, 接下来通过2个例子的模拟, 观察一下对数据库及业务产生的影响

准备测试数据表
```
MariaDB [flask_restful]> DROP TABLE IF EXISTS `t_products`;
CREATE TABLE `t_products` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(60) NOT NULL DEFAULT '' COMMENT 'product name',
  `num` INT NOT NULL DEFAULT '0' COMMENT 'stock num',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='stock table';
MariaDB [flask_restful]> select @@global.tx_isolation, @@tx_isolation;
+-----------------------+-----------------+
| @@global.tx_isolation | @@tx_isolation  |
+-----------------------+-----------------+
| REPEATABLE-READ       | REPEATABLE-READ |
+-----------------------+-----------------+
```
InnoDB事务的隔离级别有四级，默认是“可重复读”（REPEATABLE READ）


1. 插入库存（不存在则插入）
```
T Session A                                     Session B
|
| START TRANSACTION;                            START TRANSACTION;
|
| SELECT * FROM t_products WHERE name='a';
| empty set
|                                               INSERT INTO t_products (`name`, `num`) VALUES ('a', 5);
|
| SELECT * FROM t_products;                     SELECT * FROM t_products WHERE name='a';
| empty set                                     +----+------+-----+
|                                               | id | name | num |
|                                               +----+------+-----+
|                                               |  1 | a    |   5 |
|                                               +----+------+-----+
|
|                                               COMMIT;
|
| SELECT * FROM t_products WHERE name='a';
| empty set
|
| INSERT INTO t_products (`name`, `num`) VALUES ('a', 5);
| ERROR 1062 (23000): Duplicate entry 'a' for key 'uk_name'
-
```
虽然因幻读导致数据库级别插入异常, 但是异常回滚不会影响业务


2. 抢购秒杀（库存存在则扣除库存数量）

假定库存为1
```
MariaDB [flask_restful]> UPDATE t_products SET num=1;
```

模拟2个用户同时抢购
```
T Session A                                         Session B
|
| START TRANSACTION;                                START TRANSACTION;
|
| SELECT num FROM t_products WHERE id=1;            SELECT num FROM t_products WHERE id=1;
| +-----+                                           +-----+
| | num |                                           | num |
| +-----+                                           +-----+
| |   1 |                                           |   1 |
| +-----+                                           +-----+
|
| UPDATE t_products SET num=num-1 WHERE id=1 and num>0;
|
| SELECT num FROM t_products WHERE id=1;            SELECT num FROM t_products WHERE id=1;
| +-----+                                           +-----+
| | num |                                           | num |
| +-----+                                           +-----+
| |   0 |                                           |   1 |
| +-----+                                           +-----+
|
| COMMIT;
|
|                                                   SELECT num FROM t_products WHERE id=1;
|                                                   +-----+
|                                                   | num |
|                                                   +-----+
|                                                   |   1 |
|                                                   +-----+
|
|                                                   UPDATE t_products SET num=num-1 WHERE id=1 and num>0;
|
|                                                   SELECT num FROM t_products WHERE id=1;
|                                                   +-----+
|                                                   | num |
|                                                   +-----+
|                                                   |  -1 |
|                                                   +-----+
|
|                                                   COMMIT;
|
-
```
因幻读, 并没有导致数据库更新异常, 但是出现了库存超卖的现象, 即业务层面的异常

如何避免, 通过悲观锁（FOR UPDATE）方式处理:
```
MariaDB [flask_restful]> UPDATE t_products SET num=1;

T Session A                                         Session B
|
| START TRANSACTION;                                START TRANSACTION;
|
| SELECT num FROM t_products WHERE id=1 FOR UPDATE;
| +-----+
| | num |
| +-----+
| |   1 |
| +-----+
|
|                                                   SELECT num FROM t_products WHERE id=1 FOR UPDATE;
|                                                   等待...直到超时, 当其他事物提交返回更新后的结果
|
| UPDATE t_products SET num=num-1 WHERE id=1 and num>0;
|
| SELECT num FROM t_products WHERE id=1;
| +-----+
| | num |
| +-----+
| |   0 |
| +-----+
|
| COMMIT;
|
|                                                   +-----+
|                                                   | num |
|                                                   +-----+
|                                                   |   0 |
|                                                   +-----+
|
|                                                   UPDATE t_products SET num=num-1 WHERE id=1 and num>0;
|
|                                                   SELECT num FROM t_products WHERE id=1;
|                                                   +-----+
|                                                   | num |
|                                                   +-----+
|                                                   |   0 |
|                                                   +-----+
|
|                                                   COMMIT;
|
-
```
通过悲观锁的方式, 可以防止高并发场景下的超卖现象

如果指定主键, 为行级别锁, 否则为表级别锁


## Flask + Sqlalchemy 测试

1. 默认不加锁
```
inventory_obj = db.session.query(Inventory).filter(Inventory.id == inventory_id)
import time
time.sleep(2)
if inventory_obj.one().stock_qty >= num:
    time.sleep(2)
    data = {
        'stock_qty': Inventory.stock_qty - num
    }
    inventory_obj.update(data)
    db.session.commit()
return True
```
出现超卖现象

2. 加悲观锁/排它锁（with_for_update）
```
inventory_obj = db.session.query(Inventory).filter(Inventory.id == inventory_id)
import time
time.sleep(2)
if inventory_obj.with_for_update().one().stock_qty >= num:
    time.sleep(2)
    data = {
        'stock_qty': Inventory.stock_qty - num
    }
    inventory_obj.update(data)
    db.session.commit()
return True
```
一切正常, 没有超卖, 会阻塞其它事务, 性能较差

3. 分布式锁（Redis方案）

TODO


## 死锁

说到锁, 必然要考虑死锁的情况

应避免非主键条件的更新操作


## OLTP 和 OLAP

- OLTP On-Line Transaction Processing 联机事务处理
- OLAP On-Line Analytical Processing 联机分析处理

已有的两个主流开源数据库，MySQL和PostgreSQL都是针对OLTP环境的，在OLAP在线分析需求下它们的性能明显不足。


## ETL

ETL，Extraction-Transformation-Loading的缩写，即数据抽取（Extract）、转换（Transform）、装载（Load）的过程，它是构建数据仓库的重要环节。
