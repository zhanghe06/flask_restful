#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: customer.py
@time: 2018-07-05 16:57
"""

from __future__ import unicode_literals

from flask import jsonify, make_response
from flask_restful import Resource, marshal, reqparse

from web_api.bearings.outputs.customer import fields_item_customer, fields_detail_customer
from web_api.bearings.reqparsers.customer import (
    request_parser,
    request_parser_item_post,
    request_parser_item_put,
    structure_key_item,
    structure_key_items,
)
from web_api.commons.exceptions import BadRequest, NotFound
from web_api.bearings.apis.customer import (
    get_customer_row_by_id,
    get_customer_detail_info,
    edit_customer,
    delete_customer,
    get_customer_limit_rows_by_last_id,
    add_customer,
    get_customer_pagination,
)
from web_api.commons.http_token_auth import token_auth
from web_api import app

SUCCESS_MSG = app.config['SUCCESS_MSG']
FAILURE_MSG = app.config['FAILURE_MSG']


class CustomerResource(Resource):
    """
    CustomerResource
    """
    decorators = [token_auth.login_required]

    def get(self, pk):
        """
        Example:
            curl http://0.0.0.0:5000/bearings/customer/1
        :param pk:
        :return:
        """
        data = get_customer_detail_info(pk)
        if not data:
            raise NotFound
        result = marshal(data, fields_detail_customer, envelope=structure_key_item)
        return jsonify(result)

    def delete(self, pk):
        """
        Example:
            curl http://0.0.0.0:5000/bearings/customer/1 -X DELETE
        :param pk:
        :return:
        """
        # TODO Soft Delete with delete time
        result = delete_customer(pk)
        if result:
            success_msg = SUCCESS_MSG.copy()
            return make_response(jsonify(success_msg), 204)
        else:
            failure_msg = FAILURE_MSG.copy()
            return make_response(jsonify(failure_msg), 400)

    def put(self, pk):
        """
        Example:
            curl http://0.0.0.0:5000/bearings/customer/1 -H "Content-Type: application/json" -X PUT -d '
            {
                "customer": {
                    "company_name": "测试公司a",
                    "company_tel": "021-62345678",
                    "company_fax": "021-62345678"
                }
            }'
        :param pk:
        :return:
        """
        request_args = request_parser.parse_args()
        request_item_args = request_parser_item_put.parse_args(req=request_args)
        if not request_item_args:
            raise BadRequest('Bad request.')

        request_data = request_item_args
        # TODO with update time
        result = edit_customer(pk, request_data)
        if result:
            success_msg = SUCCESS_MSG.copy()
            return make_response(jsonify(success_msg), 200)
        else:
            failure_msg = FAILURE_MSG.copy()
            return make_response(jsonify(failure_msg), 400)


class CustomerListResource(Resource):
    """
    CustomerListResource
    """
    decorators = [token_auth.login_required]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:5000/bearings/customers
            curl http://0.0.0.0:5000/bearings/customers?last_pk=2&limit_num=2
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('last_pk', type=int, default=0, location='args')
        filter_parser.add_argument('limit_num', type=int, default=20, location='args')

        filter_parser_args = filter_parser.parse_args()

        data = get_customer_limit_rows_by_last_id(**filter_parser_args)
        result = marshal(data, fields_item_customer, envelope=structure_key_items)
        return jsonify(result)

    def post(self):
        """
        Example:
            curl http://0.0.0.0:5000/bearings/customers -H "Content-Type: application/json" -X POST -d '
            {
                "customer": {
                    "company_name": "测试公司_test",
                    "company_type": 1,
                    "owner_uid": 1,
                    "company_address": "公司地址1",
                    "company_site": "http://www.baidu.com",
                    "company_tel": "021-62345678",
                    "company_fax": "021-62345678"
                }
            }'
        :return:
        """
        request_args = request_parser.parse_args()
        request_item_args = request_parser_item_post.parse_args(req=request_args)
        if not request_item_args:
            raise BadRequest('Bad request.')

        request_data = request_item_args
        result = add_customer(request_data)
        if result:
            SUCCESS_MSG['id'] = result
            return make_response(jsonify(SUCCESS_MSG), 201)
        raise NotFound


class CustomerPaginationResource(Resource):
    """
    CustomerPaginationResource
    """
    decorators = [token_auth.login_required]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:5000/bearings/customers/pagination
            curl http://0.0.0.0:5000/bearings/customers/pagination?page=2&per_page=2
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('page', type=int, default=1, location='args')
        filter_parser.add_argument('per_page', type=int, default=20, location='args')

        filter_parser_args = filter_parser.parse_args()

        pagination_obj = get_customer_pagination(**filter_parser_args)

        result = marshal(pagination_obj.items, fields_item_customer, envelope=structure_key_items)
        result['total'] = pagination_obj.total
        return jsonify(result)
