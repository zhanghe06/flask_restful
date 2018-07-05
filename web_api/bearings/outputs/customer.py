#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: customer.py
@time: 2018-07-05 16:57
"""


from __future__ import unicode_literals

from flask_restful import fields
from web_api.bearings.outputs.customer_contact import fields_item_customer_contact
from web_api.bearings.outputs.customer_invoice import fields_item_customer_invoice


# 客户详情
fields_item_customer = {
    'id': fields.Integer,
    'company_name': fields.String,
    'company_address': fields.String,
    'company_site': fields.String,
    'company_tel': fields.String,
    'company_fax': fields.String,
    'company_type': fields.Integer,
    'owner_uid': fields.Integer,
    'status_delete': fields.Boolean,
    'delete_time': fields.DateTime(dt_format=b'iso8601'),
    'create_time': fields.DateTime(dt_format=b'iso8601'),
    'update_time': fields.DateTime(dt_format=b'iso8601'),
}

# 客户详情
fields_detail_customer = fields_item_customer.copy()
fields_detail_customer['customer_contacts'] = fields.List(fields.Nested(fields_item_customer_contact))
fields_detail_customer['customer_invoice'] = fields.Nested(fields_item_customer_invoice, allow_null=True)
