#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: bearings.py
@time: 2018-05-31 10:12
"""

from flask_sqlalchemy import SQLAlchemy

from web_api import app

db = SQLAlchemy(app)
