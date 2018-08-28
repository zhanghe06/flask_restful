## SQLAlchemy

[SQLAlchemy Documentation](http://docs.sqlalchemy.org/en/latest)


### Conjunctions

[Conjunctions](http://docs.sqlalchemy.org/en/latest/core/tutorial.html#conjunctions)

- and_()
- or_()
- not_()


### Common Filter Operators

[Common Filter Operators](http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#common-filter-operators)

- User.name == 'ed'
- User.name != 'ed'
- User.name.like('%ed%')
- User.name.in_(['ed', 'wendy', 'jack'])
- ~User.name.in_(['ed', 'wendy', 'jack'])
- User.name == None
- User.name.is_(None)
- User.name != None
- User.name.isnot(None)


### Functions

[Functions](http://docs.sqlalchemy.org/en/latest/core/tutorial.html#functions)

from sqlalchemy.sql import func

- func.now()
- func.current_timestamp()
- func.concat('x', 'y')
- func.substr(User.nickname, 2).label('nickname_new')  # SqLite
- func.left(User.nickname, 2).label('nickname_new')  # MySql
- func.date(User.create_time).label('date')
- func.count(User.id)


### Transtraction

- 基本结构

```
try:
    db.session.add(model_obj_01)
    db.session.flush()
    print inspect(model_obj_01).identity[0]
    
    db.session.add(model_obj_02)
    db.session.flush()
    print inspect(model_obj_02).identity[0]

    db.session.commit()
except Exception as e:
    db.session.rollback()
    raise e
```

db.session.flush() 是将数据修改刷入内存

db.session.commit() 将修改存入数据库


- 连接 URI 格式

[支持的数据库](http://www.sqlalchemy.org/docs/core/engines.html)

**Postgres**
```
postgresql://scott:tiger@localhost/mydatabase
```

**MySQL**
```
mysql://scott:tiger@localhost/mydatabase
```

**Oracle**
```
oracle://scott:tiger@127.0.0.1:1521/sidname
```

**SQLite** (注意开头的四个斜线)
```
sqlite:////absolute/path/to/foo.db
```


### session/连接池 的问题

先理解几个基础概念

- **session**
- **pool**
- **connection**
- **db**


```graph
graph TD

    S1(session01) --> | query | P[Connection Pool]
    S2(session02) --> | commit | P
    S3(session03) --> | rollback | P
    S4(session04) --> | close | P
    S5(session...) --> | flush | P
    SO(session other) --> O[overflow]

    P --> C1(connection01)
    P --> C2(connection02)
    P -.-> C3(connection03)
    P --> C4(connection04)
    P --> C5(connection...)
    O --> CO(connection other)

    C1 --> | connection | G((DB))
    C2 --> | connection | G((DB))
    C3 -.-> | recycle | G((DB))
    C4 --> | connection | G((DB))
    C5 --> | connection | G((DataBase))
    CO --> | connection | G((DataBase))
```


http://einverne.github.io/post/2017/05/sqlalchemy-session.html

1. 干脆禁用连接池（NullPool）如果session对象被析构但是没有被调用session.close(), 则数据库连接不会被断开, 直到程序终止。
2. 默认自动开启连接池, 就算显式地调用session.close(), 也不能把连接关闭。连接会由QueuePool连接池进行管理并复用。


create_engine()函数和连接池相关的参数:

- **pool_recycle**, 默认为-1, 推荐设置为7200, 即如果connection空闲了7200秒, 自动重新获取, 以防止connection被db server关闭.
- **pool_size**, 连接数大小，默认为5，正式环境该数值太小，需根据实际情况调大
- **max_overflow**, 超出pool_size后可允许的最大连接数，默认为10, 这10个连接在使用过后, 不放在pool中, 而是被真正关闭的.
- **pool_timeout**, 获取连接的超时阈值, 默认为30秒


### 排它锁/悲观锁

http://docs.sqlalchemy.org/en/latest/orm/query.html?highlight=update#sqlalchemy.orm.query.Query.with_for_update


### TODO

- [ ] 异常模拟
