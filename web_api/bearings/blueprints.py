#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: blueprints.py
@time: 2018-06-28 00:22
"""


from flask import Blueprint

bearings_bp = Blueprint('bearings', __name__, url_prefix='/bearings')
