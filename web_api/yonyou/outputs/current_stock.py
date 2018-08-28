#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: current_stock.py
@time: 2018-08-23 14:23
"""


from __future__ import unicode_literals

from flask_restful import fields


fields_item_current_stock = {
    'id': fields.Integer(attribute='id'),
    'batch': fields.String(attribute='batch'),  # 批次
    'baseQuantity': fields.Integer(attribute='baseQuantity'),  # 数量
    'id_inventory': fields.Integer(attribute='idinventory'),  # 产品id
    'id_baseunit': fields.Integer(attribute='idbaseunit'),  # 单位id
    'id_warehouse': fields.Integer(attribute='idwarehouse'),  # 仓库id
    'create_time': fields.DateTime(dt_format=b'iso8601', attribute='createdtime'),
    'update_time': fields.DateTime(dt_format=b'iso8601', attribute='updated'),
}

fields_item_current_stock_cn = {
    '主键': fields.Integer(attribute='id'),
    '批次': fields.String(attribute='batch'),  # 批次
    '数量': fields.Integer(attribute='baseQuantity'),  # 数量
    '产品': fields.Integer(attribute='idinventory'),  # 产品id
    '单位': fields.Integer(attribute='idbaseunit'),  # 单位id
    '仓库': fields.Integer(attribute='idwarehouse'),  # 仓库id
    '创建时间': fields.DateTime(dt_format=b'iso8601', attribute='createdtime'),
    '更细时间': fields.DateTime(dt_format=b'iso8601', attribute='updated'),
}
