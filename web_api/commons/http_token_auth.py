#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: http_token_auth.py
@time: 2018-06-21 10:52
"""


from flask_httpauth import HTTPTokenAuth
from itsdangerous import SignatureExpired, BadSignature

from web_api.commons.exceptions import TokenError, TokenExpired, TokenNotExist

from libs.auth_token import verify_auth_token


token_auth = HTTPTokenAuth(scheme='Bearer')


@token_auth.verify_token
def verify_token(token):
    if not token:
        raise TokenNotExist
    try:
        return verify_auth_token(token)
    except SignatureExpired:
        raise TokenExpired
    except BadSignature:
        raise TokenError
