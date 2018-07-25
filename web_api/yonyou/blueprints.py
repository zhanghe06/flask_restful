#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: blueprints.py
@time: 2018-07-24 00:14
"""


from flask import Blueprint

yonyou_bp = Blueprint('yonyou', __name__, url_prefix='/yonyou')
