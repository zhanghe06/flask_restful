#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: partner.py
@time: 2018-07-24 00:30
"""


from __future__ import unicode_literals

from flask_restful import fields

fields_item_partner = {
    'id': fields.Integer(attribute='id'),
    'code': fields.String(attribute='code'),
    'name': fields.String(attribute='name'),
    'type_partner': fields.Integer(attribute='partnerType'),
    'id_settle': fields.Integer(attribute='idsettlementPartner'),  # 结算客户id
    'advr_balance': fields.Float(attribute='AdvRBalance'),  # 预收余额
    'advp_balance': fields.Float(attribute='AdvPBalance'),  # 预付余额
    'ar_balance': fields.Float(attribute='aRBalance'),  # 应收余额
    'ap_balance': fields.Float(attribute='aPBalance'),  # 应付余额
    'disabled': fields.Integer(attribute='disabled'),
    'id_sales': fields.Integer(attribute='idsaleman'),
    'address': fields.String(attribute='ShipmentAddress'),
    'contact': fields.String(attribute='Contact'),
    'mobile': fields.String(attribute='MobilePhone'),
    'tel': fields.String(attribute='TelephoneNo'),
    'fax': fields.String(attribute='Fax'),
    'create_time': fields.DateTime(dt_format=b'iso8601', attribute='createdTime'),
    'update_time': fields.DateTime(dt_format=b'iso8601', attribute='updated'),
}

fields_item_partner_cn = {
    '主键': fields.Integer(attribute='id'),
    '编号': fields.String(attribute='code'),
    '名称': fields.String(attribute='name'),
    '类型': fields.Integer(attribute='partnerType'),
    '结算单位': fields.Integer(attribute='idsettlementPartner'),  # 结算客户id
    '预收余额': fields.Float(attribute='AdvRBalance'),  # 预收余额
    '预付余额': fields.Float(attribute='AdvPBalance'),  # 预付余额
    '应收余额': fields.Float(attribute='aRBalance'),  # 应收余额
    '应付余额': fields.Float(attribute='aPBalance'),  # 应付余额
    '是否禁用': fields.Integer(attribute='disabled'),
    '分管人员': fields.Integer(attribute='idsaleman'),
    '收货地址': fields.String(attribute='ShipmentAddress'),
    '联系人员': fields.String(attribute='Contact'),
    '手机': fields.String(attribute='MobilePhone'),
    '电话': fields.String(attribute='TelephoneNo'),
    '传真': fields.String(attribute='Fax'),
    '创建时间': fields.DateTime(dt_format=b'iso8601', attribute='createdTime'),
    '更细时间': fields.DateTime(dt_format=b'iso8601', attribute='updated'),
}
