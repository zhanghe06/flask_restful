# MSSqlServer

系统: Win Server 2008 R2 X64

开启 .NET Framework
```
开始 >> 管理工具 >> 服务器管理器 >> 功能 >> 添加功能 >> 勾选 .NET Framework 3.5.1 >> 下一步 >> 安装
```

服务端

[Microsoft® SQL Server® 2008 R2 SP2 - Express Edition](https://www.microsoft.com/zh-CN/download/details.aspx?id=30438)

客户端

[Microsoft SQL Server 2008 R2 RTM - Management Studio Express](https://www.microsoft.com/zh-CN/download/details.aspx?id=22985)

```
账号: sa
密码: 1qazXSW@
```

初始化配置
```
# 开启 TCP/IP
Sql Server Configuration Manager >> SQL Server 网络配置 >> SQLEXPRESS 的协议 >> TCP/IP 右键启用

# 开启 SQL Server Brower
Sql Server Configuration Manager >> SQL Server 配置管理器 >> SQL Server 服务
1. SQL Server Brower 右键属性 >> 服务 >> 启动模式（自动） >> 应用
2. SQL Server Brower 右键启动
```

关闭防火墙

测试远程连接

DataGrip 配置（Mac 使用jtds驱动）

参考: https://blog.jetbrains.com/datagrip/2016/06/21/connecting-datagrip-to-ms-sql-server/
```
jdbc:jtds:sqlserver://192.168.64.244:1433;instance=SQLEXPRESS
```


sqlalchemy 驱动

[http://docs.sqlalchemy.org/en/latest/dialects/mssql.html](http://docs.sqlalchemy.org/en/latest/dialects/mssql.html)

```
mssql+pymssql://<username>:<password>@<freetds_name>/?charset=utf8
```

Mac 安装 freetds(pymssql的依赖)

http://pymssql.org/en/stable/freetds.html

```
brew unlink freetds
brew install freetds@0.91
brew link --overwrite --force freetds@0.91
echo 'export PATH="/usr/local/opt/freetds@0.91/bin:$PATH"' >> ~/.zshrc
```

python 客户端 pymssql

```
pip install pymssql
```


测试连接

1. pymssql 客户端方式
```
import pymssql

conn = pymssql.connect('192.168.64.196\SQLEXPRESS', 'sa', '1qazXSW@', "UFTData018618_000666")
cursor = conn.cursor()
cursor.execute('SELECT * FROM AA_Partner')
row = cursor.fetchone()
while row:
    print("ID=%s, Name=%s" % (row[0], row[1]))
    row = cursor.fetchone()

conn.close()
```

2. sqlalchemy 方式
```
from sqlalchemy import create_engine

conn_str = 'mssql+pymssql://%s:%s@%s/UFTData018618_000666' % ('sa', '1qazXSW@', '192.168.64.196\SQLEXPRESS')
engine = create_engine(conn_str)
connection = engine.connect()
result = connection.execute("SELECT * FROM AA_Partner")
row = result.fetchone()
print("ID=%s, Name=%s" % (row[0], row[1]))
connection.close()
```
