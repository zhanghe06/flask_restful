#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test.py
@time: 2018-07-03 17:20
"""


from __future__ import unicode_literals


from flask import jsonify, make_response
from flask_restful import Resource, reqparse, inputs

from web_api import app
from web_api.bearings.apis.test import test_decrease_inventory
from web_api.commons.http_basic_auth import basic_auth

SUCCESS_MSG = app.config['SUCCESS_MSG'].copy()
FAILURE_MSG = app.config['FAILURE_MSG'].copy()


class TestDecreaseInventoryResource(Resource):
    """
    TestDecreaseInventoryResource
    """
    decorators = [basic_auth.login_required]

    def post(self, pk):
        """
        Example:
            curl http://0.0.0.0:5000/bearings/test_decrease_inventory/1?num=100&lock=true
            curl http://0.0.0.0:5000/bearings/test_decrease_inventory/1?num=100&lock=false
        :param pk:
        :return:
        """
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('num', type=int, default=1, location='args')
        filter_parser.add_argument('lock', type=inputs.boolean, default=False, location='args')

        filter_parser_args = filter_parser.parse_args()

        inventory_id = pk
        num = filter_parser_args.get('num', 1)
        lock = filter_parser_args.get('lock', False)

        result = test_decrease_inventory(inventory_id, num, lock)
        if result:
            SUCCESS_MSG['result'] = result
            return make_response(jsonify(SUCCESS_MSG), 202)
        else:
            FAILURE_MSG['result'] = result
            return make_response(jsonify(FAILURE_MSG), 400)
