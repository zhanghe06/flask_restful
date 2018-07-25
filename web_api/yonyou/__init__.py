#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2018-07-24 00:12
"""


from web_api.yonyou.blueprints import yonyou_bp
from flask_restful import Api
from web_api.commons.exceptions import errors

yonyou_api = Api(yonyou_bp, errors=errors)
