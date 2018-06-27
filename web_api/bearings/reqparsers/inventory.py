#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: inventory.py
@time: 2018-07-04 10:25
"""


from __future__ import unicode_literals

from flask_restful import reqparse, inputs


structure_key_item = 'inventory'
structure_key_items = 'inventories'

request_parser = reqparse.RequestParser()
request_parser.add_argument(structure_key_item, type=dict, location='json')

request_parser_item = reqparse.RequestParser(trim=True, bundle_errors=True)


# POST
request_parser_item_post = request_parser_item.copy()

request_parser_item_post.add_argument(
    name='product_id',
    type=int,
    location=structure_key_item,
    store_missing=False,
    required=True
)
request_parser_item_post.add_argument(
    name='warehouse_id',
    type=int,
    location=structure_key_item,
    store_missing=False,
    required=True
)
request_parser_item_post.add_argument(
    name='rack_id',
    type=int,
    location=structure_key_item,
    store_missing=False,
    required=True
)
request_parser_item_post.add_argument(
    name='stock_qty',
    type=int,
    location=structure_key_item,
    store_missing=False,
    required=True
)
request_parser_item_post.add_argument(
    name='note',
    location=structure_key_item,
    store_missing=False,
    required=False
)
request_parser_item_post.add_argument(
    name='status_delete',
    type=inputs.boolean,
    location=structure_key_item,
    store_missing=False,
    required=False
)
request_parser_item_post.add_argument(
    name='delete_time',
    type=inputs.datetime,
    location=structure_key_item,
    store_missing=False,
    required=False
)
request_parser_item_post.add_argument(
    'create_time',
    type=inputs.datetime,
    location=structure_key_item,
    store_missing=False,
    required=False
)
request_parser_item_post.add_argument(
    'update_time',
    type=inputs.datetime,
    location=structure_key_item,
    store_missing=False,
    required=False
)

# PUT
request_parser_item_put = request_parser_item.copy()
request_parser_item_put.add_argument(
    name='product_id',
    location=structure_key_item,
    store_missing=False,
    required=True
)
request_parser_item_put.add_argument(
    name='warehouse_id',
    location=structure_key_item,
    store_missing=False,
    required=True
)
request_parser_item_put.add_argument(
    name='rack_id',
    location=structure_key_item,
    store_missing=False,
    required=True
)
request_parser_item_put.add_argument(
    name='stock_qty',
    location=structure_key_item,
    store_missing=False,
    required=True
)
request_parser_item_put.add_argument(
    name='note',
    location=structure_key_item,
    store_missing=False,
    required=False
)
request_parser_item_put.add_argument(
    name='status_delete',
    type=inputs.boolean,
    location=structure_key_item,
    store_missing=False,
    required=False
)
request_parser_item_put.add_argument(
    name='delete_time',
    type=inputs.datetime,
    location=structure_key_item,
    store_missing=False,
    required=False
)
request_parser_item_put.add_argument(
    'create_time',
    type=inputs.datetime,
    location=structure_key_item,
    store_missing=False,
    required=False
)
request_parser_item_put.add_argument(
    'update_time',
    type=inputs.datetime,
    location=structure_key_item,
    store_missing=False,
    required=False
)
