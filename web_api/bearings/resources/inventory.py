#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: inventory.py
@time: 2018-06-28 00:22
"""


from __future__ import unicode_literals

from flask import jsonify, make_response
from flask_restful import Resource, marshal, reqparse

from web_api.bearings.outputs.inventory import fields_item
from web_api.bearings.reqparsers.inventory import (
    request_parser,
    request_parser_item_post,
    request_parser_item_put,
    structure_key_item,
    structure_key_items,
)
from web_api.commons.exceptions import BadRequest, NotFound
from web_api.bearings.apis.inventory import (
    get_inventory_row_by_id,
    edit_inventory,
    delete_inventory,
    get_inventory_limit_rows_by_last_id,
    add_inventory,
    get_inventory_pagination,
    increase_inventory,
)
from web_api.commons.http_token_auth import token_auth
from web_api import app

SUCCESS_MSG = app.config['SUCCESS_MSG']
FAILURE_MSG = app.config['FAILURE_MSG']


class InventoryResource(Resource):
    """
    InventoryResource
    """
    decorators = [token_auth.login_required]

    def get(self, pk):
        """
        Example:
            curl http://0.0.0.0:5000/bearings/inventory/1
        :param pk:
        :return:
        """
        data = get_inventory_row_by_id(pk)
        if not data:
            raise NotFound
        result = marshal(data, fields_item, envelope=structure_key_item)
        return jsonify(result)

    def delete(self, pk):
        """
        Example:
            curl http://0.0.0.0:5000/bearings/inventory/1 -X DELETE
        :param pk:
        :return:
        """
        result = delete_inventory(pk)
        if result:
            success_msg = SUCCESS_MSG.copy()
            return make_response(jsonify(success_msg), 204)
        else:
            failure_msg = FAILURE_MSG.copy()
            return make_response(jsonify(failure_msg), 400)

    def put(self, pk):
        """
        Example:
            curl http://0.0.0.0:5000/bearings/inventory/1 -H "Content-Type: application/json" -X PUT -d '
            {
                "inventory": {
                    "product_id": 1,
                    "warehouse_id": 1,
                    "rack_id": 1,
                    "stock_qty": 101
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
        result = edit_inventory(pk, request_data)
        if result:
            success_msg = SUCCESS_MSG.copy()
            return make_response(jsonify(success_msg), 200)
        else:
            failure_msg = FAILURE_MSG.copy()
            return make_response(jsonify(failure_msg), 400)


class InventoryListResource(Resource):
    """
    InventoryListResource
    """
    decorators = [token_auth.login_required]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:5000/bearings/inventories
            curl http://0.0.0.0:5000/bearings/inventories?last_pk=2&limit_num=2
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('last_pk', type=int, default=0, location='args')
        filter_parser.add_argument('limit_num', type=int, default=20, location='args')

        filter_parser_args = filter_parser.parse_args()

        data = get_inventory_limit_rows_by_last_id(**filter_parser_args)
        result = marshal(data, fields_item, envelope=structure_key_items)
        return jsonify(result)

    def post(self):
        """
        Example:
            curl http://0.0.0.0:5000/bearings/inventories -H "Content-Type: application/json" -X POST -d '
            {
                "inventory": {
                    "product_id": 1,
                    "warehouse_id": 1,
                    "rack_id": "1",
                    "stock_qty": 100,
                    "note": "SNFA"
                }
            }'
        :return:
        """
        request_args = request_parser.parse_args()
        request_item_args = request_parser_item_post.parse_args(req=request_args)
        if not request_item_args:
            raise BadRequest('Bad request.')

        request_data = request_item_args
        result = add_inventory(request_data)
        if result:
            SUCCESS_MSG['id'] = result
            return make_response(jsonify(SUCCESS_MSG), 201)
        raise NotFound


class InventoryPaginationResource(Resource):
    """
    InventoryPaginationResource
    """
    decorators = [token_auth.login_required]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:5000/bearings/inventories/pagination
            curl http://0.0.0.0:5000/bearings/inventories/pagination?page=2&per_page=2
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('page', type=int, default=1, location='args')
        filter_parser.add_argument('per_page', type=int, default=20, location='args')

        filter_parser_args = filter_parser.parse_args()

        pagination_obj = get_inventory_pagination(**filter_parser_args)

        result = marshal(pagination_obj.items, fields_item, envelope=structure_key_items)
        result['total'] = pagination_obj.total
        return jsonify(result)
