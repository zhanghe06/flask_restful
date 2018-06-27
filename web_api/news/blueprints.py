#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: blueprints.py
@time: 2018-05-31 18:01
"""


from flask import Blueprint

news_bp = Blueprint('news', __name__, url_prefix='/news')
