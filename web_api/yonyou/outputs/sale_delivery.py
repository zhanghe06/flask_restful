#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: sale_delivery.py
@time: 2018-07-24 16:58
"""


from __future__ import unicode_literals

from flask_restful import fields

fields_item_sale_delivery = {
    'id': fields.Integer(attribute='ID'),
    'code': fields.String(attribute='code'),
    'id_customer': fields.Integer(attribute='idcustomer'),  # 客户id
    'id_settle': fields.Integer(attribute='idsettlecustomer'),  # 结算客户id
    'is_sale_out': fields.Integer(attribute='isSaleOut'),
    'recive_type': fields.Integer(attribute='reciveType'),
    'amount': fields.Float(attribute='amount'),
    'amount_tax': fields.Float(attribute='taxAmount'),
    'receive_balance': fields.Float(attribute='ReceiveBalance'),
    'makerid': fields.Integer(attribute='makerid'),
    'maker': fields.String(attribute='maker'),
    'create_time': fields.DateTime(dt_format=b'iso8601', attribute='createdtime'),
    'update_time': fields.DateTime(dt_format=b'iso8601', attribute='updated'),
}

fields_item_sale_delivery_cn = {
    '主键': fields.Integer(attribute='ID'),
    '编号': fields.String(attribute='code'),
    '客户': fields.Integer(attribute='idcustomer'),  # 客户id
    '结算单位': fields.Integer(attribute='idsettlecustomer'),  # 结算客户id
    '出库状态': fields.Integer(attribute='isSaleOut'),
    '收款方式': fields.Integer(attribute='reciveType'),
    '金额': fields.Float(attribute='amount'),
    '含税金额': fields.Float(attribute='taxAmount'),
    '应收余额': fields.Float(attribute='ReceiveBalance'),
    '制单人ID': fields.Integer(attribute='makerid'),
    '制单人': fields.String(attribute='maker'),
    '创建时间': fields.DateTime(dt_format=b'iso8601', attribute='createdtime'),
    '更细时间': fields.DateTime(dt_format=b'iso8601', attribute='updated'),
}
