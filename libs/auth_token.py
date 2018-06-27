#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: auth_token.py
@time: 2018-06-21 10:52
"""


from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from config import current_config

SECRET_KEY = current_config.SECRET_KEY
TOKEN_TTL = current_config.TOKEN_TTL


def generate_auth_token(user_id):
    s = Serializer(SECRET_KEY, expires_in=TOKEN_TTL)
    return s.dumps({'user_id': user_id})


def verify_auth_token(token):
    s = Serializer(SECRET_KEY)
    data = s.loads(token)
    return data
