#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: default.py
@time: 2018-05-30 19:02
"""


from __future__ import print_function
from __future__ import unicode_literals

import os
import binascii


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

HOST = '0.0.0.0'
DEBUG = True
SECRET_KEY = 'c9a6b2eb758aab3e1899576e76d72550cb3dd6d7a4b56b66'

TOKEN_TTL = 600

# requests 超时设置
REQUESTS_TIME_OUT = (30, 30)


# 数据库 MySQL - 用友
DB_MYSQL_YONYOU = {
    'host': '192.168.64.149\SQLEXPRESS',
    'username': 'sa',
    'password': '1qazXSW@',
    'port': 1433,
    'db': 'UFTData018618_000666'
}
SQLALCHEMY_DATABASE_URI_YONYOU = 'mssql+pymssql://%(username)s:%(password)s@%(host)s/%(db)s?charset=utf8' % DB_MYSQL_YONYOU

# 数据库 MySQL - news
DB_MYSQL_NEWS = {
    'host': HOST,
    'user': 'root',
    'passwd': '123456',
    'port': 3306,
    'db': 'news_spider'
}
SQLALCHEMY_DATABASE_URI_NEWS = 'mysql+mysqldb://%(user)s:%(passwd)s@%(host)s:%(port)s/%(db)s?charset=utf8' % DB_MYSQL_NEWS

# 数据库 MySQL - bearings
DB_MYSQL_BEARINGS = {
    'host': HOST,
    'user': 'root',
    'passwd': '123456',
    'port': 3306,
    'db': 'bearing_project'
}
SQLALCHEMY_DATABASE_URI_BEARINGS = 'mysql+mysqldb://%(user)s:%(passwd)s@%(host)s:%(port)s/%(db)s?charset=utf8' % DB_MYSQL_BEARINGS

SQLALCHEMY_BINDS = {
    'news': SQLALCHEMY_DATABASE_URI_NEWS,
    'bearings': SQLALCHEMY_DATABASE_URI_BEARINGS,
    'yonyou': SQLALCHEMY_DATABASE_URI_YONYOU
}

# SQLALCHEMY_DATABASE_URI = \
#     'mysql+mysqldb://%s:%s@%s:%s/%s?charset=utf8' % \
#     (DB_MYSQL['user'], DB_MYSQL['passwd'], DB_MYSQL['host'], DB_MYSQL['port'], DB_MYSQL['db'])
#
# # 主从配置（暂不启用）
# SQLALCHEMY_DATABASE_URI_MASTER = SQLALCHEMY_DATABASE_URI
# SQLALCHEMY_DATABASE_URI_SLAVE = SQLALCHEMY_DATABASE_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_POOL_SIZE = 5  # 默认 pool_size=5
# SQLALCHEMY_MAX_OVERFLOW = 10  # 默认 10 连接池达到最大值后可以创建的连接数
# SQLALCHEMY_POOL_TIMEOUT = 10  # 默认 10秒
SQLALCHEMY_POOL_RECYCLE = 500  # 配置要小于 数据库配置 wait_timeout
SQLALCHEMY_ECHO = False

# 缓存，队列
REDIS = {
    'host': HOST,
    'port': 6379,
    # 'password': '123456'  # redis-cli AUTH 123456
}

REDIS_URL = 'redis://:%s@%s' % (REDIS['password'], REDIS['host']) \
    if REDIS.get('password') else 'redis://%s' % REDIS['host']

CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL


SUCCESS_MSG = {
    'result': True,
    'msg': '',
}

FAILURE_MSG = {
    'result': False,
    'msg': '',
}


if __name__ == '__main__':
    sk = os.urandom(24)
    print(sk)
    print(binascii.b2a_hex(sk))
