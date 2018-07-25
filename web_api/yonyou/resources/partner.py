#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: partner.py
@time: 2018-07-24 00:24
"""


from __future__ import unicode_literals

from flask import jsonify, make_response
from flask_restful import Resource, marshal, reqparse

from web_api.yonyou.outputs.partner import fields_item_partner, fields_item_partner_cn
from web_api.yonyou.reqparsers.partner import (
    structure_key_item,
    structure_key_items,
    structure_key_item_cn,
    structure_key_items_cn,
)

from web_api.commons.exceptions import BadRequest, NotFound
from web_api.yonyou.apis.partner import (
    get_partner_row_by_id,
    edit_partner,
    delete_partner,
    get_partner_limit_rows_by_last_id,
    add_partner,
    get_partner_pagination,
)
from web_api.commons.http_token_auth import token_auth
from web_api import app

SUCCESS_MSG = app.config['SUCCESS_MSG']
FAILURE_MSG = app.config['FAILURE_MSG']


class PartnerResource(Resource):
    """
    PartnerResource
    """
    decorators = [token_auth.login_required]

    def get(self, pk):
        """
        Example:
            curl http://0.0.0.0:5000/yonyou/partner/1
        :param pk:
        :return:
        """
        data = get_partner_row_by_id(pk)
        if not data:
            raise NotFound
        result = marshal(data, fields_item_partner_cn, envelope=structure_key_item_cn)
        return jsonify(result)

    def delete(self, pk):
        """
        Example:
            curl http://0.0.0.0:5000/yonyou/partner/1 -X DELETE
        :param pk:
        :return:
        """
        result = delete_partner(pk)
        if result:
            success_msg = SUCCESS_MSG.copy()
            return make_response(jsonify(success_msg), 204)
        else:
            failure_msg = FAILURE_MSG.copy()
            return make_response(jsonify(failure_msg), 400)


class PartnerListResource(Resource):
    """
    PartnerListResource
    """
    decorators = [token_auth.login_required]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:5000/yonyou/partners
            curl http://0.0.0.0:5000/yonyou/partners?last_pk=1000&limit_num=2
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('last_pk', type=int, default=0, location='args')
        filter_parser.add_argument('limit_num', type=int, default=20, location='args')

        filter_parser_args = filter_parser.parse_args()

        # data = get_partner_rows()
        data = get_partner_limit_rows_by_last_id(**filter_parser_args)
        result = marshal(data, fields_item_partner, envelope=structure_key_items_cn)
        return jsonify(result)


class PartnerPaginationResource(Resource):
    """
    PartnerPaginationResource
    """
    decorators = [token_auth.login_required]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:5000/yonyou/partners/pagination
            curl http://0.0.0.0:5000/yonyou/partners/pagination?page=2000&per_page=2
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('page', type=int, default=1, location='args')
        filter_parser.add_argument('per_page', type=int, default=20, location='args')

        filter_parser_args = filter_parser.parse_args()

        pagination_obj = get_partner_pagination(**filter_parser_args)

        result = marshal(pagination_obj.items, fields_item_partner, envelope=structure_key_items)
        result['total'] = pagination_obj.total
        return jsonify(result)
