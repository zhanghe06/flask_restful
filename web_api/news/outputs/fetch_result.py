#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: fetch_result.py
@time: 2018-05-30 19:34
"""


from __future__ import unicode_literals

from flask_restful import fields

fields_item = {
    'id': fields.Integer,
    'task_id': fields.Integer,
    'platform_id': fields.Integer,
    'platform_name': fields.String,
    'channel_id': fields.Integer,
    'channel_name': fields.String,
    'article_id': fields.String,
    'article_url': fields.String,
    'article_title': fields.String,
    'article_author_id': fields.String,
    'article_author_name': fields.String,
    'article_tags': fields.String,
    'article_abstract': fields.String,
    'article_content': fields.String,
    'article_pub_time': fields.DateTime(dt_format=b'iso8601'),
    'create_time': fields.DateTime(dt_format=b'iso8601'),
    'update_time': fields.DateTime(dt_format=b'iso8601'),
}
