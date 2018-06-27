#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: resources.py
@time: 2018-06-21 16:46
"""


from __future__ import unicode_literals

from flask import jsonify
from flask_restful import Resource

from libs.auth_token import generate_auth_token
from web_api.commons.http_basic_auth import basic_auth
from web_api import app
from uuid import uuid4

SUCCESS_MSG = app.config['SUCCESS_MSG']


class TokenResource(Resource):
    """
    TokenResource
    """
    decorators = [basic_auth.login_required]

    # @basic_auth.login_required
    def get(self):
        """
        get
        Example:
            curl http://0.0.0.0:5000/token
            curl -u username:password http://0.0.0.0:5000/token
            curl -H "Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=" http://0.0.0.0:5000/token
        :return:
        """
        success_msg = SUCCESS_MSG.copy()
        success_msg['token'] = generate_auth_token(uuid4().get_hex())
        return jsonify(success_msg)
