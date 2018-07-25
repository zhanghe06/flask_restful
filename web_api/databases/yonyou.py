#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: yonyou.py
@time: 2018-07-24 00:10
"""

from flask_sqlalchemy import SQLAlchemy

from web_api import app

db = SQLAlchemy(app)
