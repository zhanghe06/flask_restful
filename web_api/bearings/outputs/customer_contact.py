#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: customer_contact.py
@time: 2018-07-05 17:54
"""


from __future__ import unicode_literals

from flask_restful import fields


# 客户联系方式
fields_item_customer_contact = {
    'id': fields.Integer,
    'cid': fields.Integer,
    'name': fields.String,
    'salutation': fields.String,
    'mobile': fields.String,
    'tel': fields.String,
    'fax': fields.String,
    'department': fields.String,
    'address': fields.String,
    'note': fields.String,
    'status_default': fields.Boolean,
    'status_delete': fields.Boolean,
    'delete_time': fields.DateTime(dt_format=b'iso8601'),
    'create_time': fields.DateTime(dt_format=b'iso8601'),
    'update_time': fields.DateTime(dt_format=b'iso8601'),
}
