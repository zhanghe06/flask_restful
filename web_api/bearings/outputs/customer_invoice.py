#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: customer_invoice.py
@time: 2018-07-05 17:54
"""


from __future__ import unicode_literals

from flask_restful import fields


# 客户开票资料
fields_item_customer_invoice = {
    'cid': fields.Integer,
    'company_name': fields.String,
    'company_tax_id': fields.String,
    'company_address': fields.String,
    'company_tel': fields.String,
    'company_bank_name': fields.String,
    'company_bank_account': fields.String,
    'status_delete': fields.Boolean,
    'delete_time': fields.DateTime(dt_format=b'iso8601'),
    'create_time': fields.DateTime(dt_format=b'iso8601'),
    'update_time': fields.DateTime(dt_format=b'iso8601'),
}
