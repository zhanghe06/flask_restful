#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: http_basic_auth.py
@time: 2018-06-21 10:49
"""

from flask_httpauth import HTTPBasicAuth

from web_api.commons.exceptions import Unauthorized

basic_auth = HTTPBasicAuth()


@basic_auth.verify_password
def verify_password(username, password):
    # user = User.query.filter_by(username = username).first()
    # if not user or not user.verify_password(password):
    #     return False
    # g.user = user
    if username != 'username' or password != 'password':
        raise Unauthorized
    return True

#
# @basic_auth.error_handler
# def unauthorized():
#     raise Unauthorized
