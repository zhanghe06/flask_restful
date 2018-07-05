#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: customer.py
@time: 2018-07-05 16:57
"""


from __future__ import unicode_literals

from flask_restful import reqparse, inputs


structure_key_item = 'customer'
structure_key_items = 'customers'

request_parser = reqparse.RequestParser()
request_parser.add_argument(structure_key_item, type=dict, location='json')

request_parser_item = reqparse.RequestParser(trim=True, bundle_errors=True)


# POST
request_parser_item_post = request_parser_item.copy()

request_parser_item_post.add_argument(
    name='company_name',
    location=structure_key_item,
    store_missing=False,
    required=True,
)
request_parser_item_post.add_argument(
    name='company_address',
    location=structure_key_item,
    store_missing=False,
    required=True,
)
request_parser_item_post.add_argument(
    name='company_site',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_post.add_argument(
    name='company_tel',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_post.add_argument(
    name='company_fax',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_post.add_argument(
    name='company_type',
    type=inputs.int_range(0, 2),
    location=structure_key_item,
    store_missing=False,
    required=True,
    help='字段必填',
)
request_parser_item_post.add_argument(
    name='owner_uid',
    type=int,
    location=structure_key_item,
    store_missing=False,
    default=0
)


# PUT
request_parser_item_put = request_parser_item.copy()

request_parser_item_put.add_argument(
    name='company_name',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    name='company_address',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    name='company_site',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    name='company_tel',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    name='company_fax',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    name='company_type',
    type=inputs.int_range(0, 2),
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    name='owner_uid',
    type=int,
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    name='status_delete',
    type=inputs.boolean,
    location=structure_key_item,
    store_missing=False,
)
