#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2018-05-30 19:08
"""


from web_api.news.blueprints import news_bp
from flask_restful import Api
from web_api.commons.exceptions import errors

news_api = Api(news_bp, errors=errors)
