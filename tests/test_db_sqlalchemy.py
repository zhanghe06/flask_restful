#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_db_sqlalchemy.py
@time: 2018-07-24 20:12
"""


from sqlalchemy import create_engine

# conn_str = 'mssql+pymssql://%s:%s@%s/UFTData018618_000666' % ('sa', '1qazXSW@', '192.168.64.167\SQLEXPRESS')
conn_str = 'mssql+pymssql://%s:%s@%s/UFTData018618_000666' % ('sa', '123456', '10.21.2.83\SQLEXPRESS')
# conn_str = 'mssql+pymssql://%s:%s@%s/UFTData78445_000666' % ('sa', 'kundi88888', '192.168.1.110')
engine = create_engine(conn_str)
connection = engine.connect()
result = connection.execute("SELECT * FROM AA_Partner")
row = result.fetchone()
print("ID=%s, Name=%s" % (row[0], row[1]))
connection.close()
