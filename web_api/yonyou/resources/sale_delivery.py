#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: sale_delivery.py
@time: 2018-07-24 16:58
"""


from __future__ import unicode_literals

from flask import jsonify, make_response
from flask_restful import Resource, marshal, reqparse

from web_api.yonyou.outputs.sale_delivery import fields_item_sale_delivery, fields_item_sale_delivery_cn
from web_api.yonyou.reqparsers.sale_delivery import (
    structure_key_item,
    structure_key_items,
    structure_key_item_cn,
    structure_key_items_cn,
)

from web_api.commons.exceptions import BadRequest, NotFound
from web_api.yonyou.apis.sale_delivery import (
    get_sale_delivery_row_by_id,
    edit_sale_delivery,
    delete_sale_delivery,
    get_sale_delivery_limit_rows_by_last_id,
    add_sale_delivery,
    get_sale_delivery_pagination,
)
from web_api.commons.http_token_auth import token_auth
from web_api import app

SUCCESS_MSG = app.config['SUCCESS_MSG']
FAILURE_MSG = app.config['FAILURE_MSG']


class SaleDeliveryResource(Resource):
    """
    SaleDeliveryResource
    """
    decorators = [token_auth.login_required]

    def get(self, pk):
        """
        Example:
            curl http://0.0.0.0:5000/yonyou/sale_delivery/1
        :param pk:
        :return:
        """
        data = get_sale_delivery_row_by_id(pk)
        if not data:
            raise NotFound
        result = marshal(data, fields_item_sale_delivery_cn, envelope=structure_key_item_cn)
        return jsonify(result)

    def delete(self, pk):
        """
        Example:
            curl http://0.0.0.0:5000/yonyou/sale_delivery/1 -X DELETE
        :param pk:
        :return:
        """
        result = delete_sale_delivery(pk)
        if result:
            success_msg = SUCCESS_MSG.copy()
            return make_response(jsonify(success_msg), 204)
        else:
            failure_msg = FAILURE_MSG.copy()
            return make_response(jsonify(failure_msg), 400)


class SaleDeliveryListResource(Resource):
    """
    SaleDeliveryListResource
    """
    decorators = [token_auth.login_required]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:5000/yonyou/sale_deliveries
            curl http://0.0.0.0:5000/yonyou/sale_deliveries?last_pk=1000&limit_num=2
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('last_pk', type=int, default=0, location='args')
        filter_parser.add_argument('limit_num', type=int, default=20, location='args')

        filter_parser_args = filter_parser.parse_args()

        # data = get_sale_delivery_rows()
        data = get_sale_delivery_limit_rows_by_last_id(**filter_parser_args)
        result = marshal(data, fields_item_sale_delivery_cn, envelope=structure_key_items_cn)
        return jsonify(result)


class SaleDeliveryPaginationResource(Resource):
    """
    SaleDeliveryPaginationResource
    """
    decorators = [token_auth.login_required]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:5000/yonyou/sale_deliveries/pagination
            curl http://0.0.0.0:5000/yonyou/sale_deliveries/pagination?page=2000&per_page=2
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('page', type=int, default=1, location='args')
        filter_parser.add_argument('per_page', type=int, default=20, location='args')

        filter_parser_args = filter_parser.parse_args()

        pagination_obj = get_sale_delivery_pagination(**filter_parser_args)

        result = marshal(pagination_obj.items, fields_item_sale_delivery, envelope=structure_key_items)
        result['total'] = pagination_obj.total
        return jsonify(result)
