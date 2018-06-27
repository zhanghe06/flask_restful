#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: urls.py
@time: 2018-06-29 11:03
"""


from uuid import uuid4
from web_api import app
from flask import jsonify, request, g

SUCCESS_MSG = app.config['SUCCESS_MSG'].copy()


@app.before_request
def api_before_request():
    g.request_id = uuid4().get_hex()


@app.after_request
def append_request_id(response):
    response.headers.add('X-Request-Id', g.request_id)
    return response


@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def heartbeat():
    return jsonify(SUCCESS_MSG)
