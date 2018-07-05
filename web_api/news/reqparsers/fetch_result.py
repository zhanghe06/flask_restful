#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: fetch_result.py
@time: 2018-05-30 19:34
"""


from __future__ import unicode_literals

from flask_restful import reqparse, inputs


structure_key_item = 'fetch_result'
structure_key_items = 'fetch_results'

request_parser = reqparse.RequestParser()
request_parser.add_argument(structure_key_item, type=dict, location='json')

request_parser_item = reqparse.RequestParser(trim=True, bundle_errors=True)


# POST
request_parser_item_post = request_parser_item.copy()

request_parser_item_post.add_argument(
    name='task_id',
    location=structure_key_item,
    store_missing=False,
    required=True,
)
request_parser_item_post.add_argument(
    name='platform_id',
    location=structure_key_item,
    store_missing=False,
    required=True,
)
request_parser_item_post.add_argument(
    name='platform_name',
    location=structure_key_item,
    store_missing=False,
    required=True,
)
request_parser_item_post.add_argument(
    name='channel_id',
    location=structure_key_item,
    store_missing=False,
    required=True,
)
request_parser_item_post.add_argument(
    name='channel_name',
    location=structure_key_item,
    store_missing=False,
    required=True,
)
request_parser_item_post.add_argument(
    name='article_id',
    location=structure_key_item,
    store_missing=False,
    required=True,
)
request_parser_item_post.add_argument(
    name='article_url',
    location=structure_key_item,
    store_missing=False,
    required=True,
)
request_parser_item_post.add_argument(
    name='article_title',
    location=structure_key_item,
    store_missing=False,
    required=True,
)
request_parser_item_post.add_argument(
    name='article_author_id',
    location=structure_key_item,
    store_missing=False,
    required=True,
)
request_parser_item_post.add_argument(
    name='article_author_name',
    location=structure_key_item,
    store_missing=False,
    required=True,
)
request_parser_item_post.add_argument(
    name='article_tags',
    location=structure_key_item,
    store_missing=False,
    required=True,
)
request_parser_item_post.add_argument(
    name='article_abstract',
    location=structure_key_item,
    store_missing=False,
    required=True,
)
request_parser_item_post.add_argument(
    name='article_content',
    location=structure_key_item,
    store_missing=False,
    required=True,
)
request_parser_item_post.add_argument(
    'article_pub_time',
    location=structure_key_item,
    store_missing=False,
    required=True,
)
request_parser_item_post.add_argument(
    'create_time',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_post.add_argument(
    'update_time',
    location=structure_key_item,
    store_missing=False,
)

# PUT
request_parser_item_put = request_parser_item.copy()
request_parser_item_put.add_argument(
    name='task_id',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    name='platform_id',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    name='platform_name',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    name='channel_id',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    name='channel_name',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    name='article_id',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    name='article_url',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    name='article_title',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    name='article_author_id',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    name='article_author_name',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    name='article_tags',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    name='article_abstract',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    name='article_content',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    'article_pub_time',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    'create_time',
    location=structure_key_item,
    store_missing=False,
)
request_parser_item_put.add_argument(
    'update_time',
    location=structure_key_item,
    store_missing=False,
)
