#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: inventory.py
@time: 2018-07-04 10:25
"""


from __future__ import unicode_literals

from flask_restful import fields

fields_item = {
    'id': fields.Integer,
    'product_id': fields.Integer,
    'warehouse_id': fields.Integer,
    'rack_id': fields.Integer,
    'stock_qty': fields.Integer,
    'note': fields.String,
    'status_delete': fields.Boolean,
    'delete_time': fields.DateTime(dt_format=b'iso8601'),
    'create_time': fields.DateTime(dt_format=b'iso8601'),
    'update_time': fields.DateTime(dt_format=b'iso8601'),
}
