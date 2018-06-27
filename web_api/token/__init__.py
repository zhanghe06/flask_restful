#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2018-06-21 16:45
"""


from web_api.token.blueprints import token_bp
from flask_restful import Api
from web_api.commons.exceptions import errors

token_api = Api(token_bp, errors=errors)
