#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: blueprints.py
@time: 2018-06-21 16:48
"""


from flask import Blueprint

token_bp = Blueprint('token', __name__, url_prefix='/token')
