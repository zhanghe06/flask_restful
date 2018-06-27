#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2018-06-28 00:20
"""


from web_api.bearings.blueprints import bearings_bp
from flask_restful import Api
from web_api.commons.exceptions import errors

bearings_api = Api(bearings_bp, errors=errors)
