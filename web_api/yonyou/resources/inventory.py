#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: inventory.py
@time: 2018-08-23 14:58
"""


from __future__ import unicode_literals

from datetime import datetime

from flask import jsonify, make_response
from flask_restful import Resource, marshal, reqparse

from web_api.yonyou.outputs.inventory import fields_item_inventory, fields_item_inventory_cn
from web_api.yonyou.reqparsers.inventory import (
    structure_key_item,
    structure_key_items,
    structure_key_item_cn,
    structure_key_items_cn,
)

from web_api.commons.exceptions import BadRequest, NotFound
from web_api.yonyou.apis.inventory import (
    get_inventory_row_by_id,
    edit_inventory,
    delete_inventory,
    get_inventory_limit_rows_by_last_id,
    add_inventory,
    get_inventory_pagination,
    get_inventory_rows,
    count_inventory,
)
from web_api.yonyou.apis.enum_items import (
    get_enum_items_row_by_id,
)

from web_api.bearings.apis.production import add_production, count_production

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
            curl http://0.0.0.0:5000/yonyou/inventory/1
        :param pk:
        :return:
        """
        data = get_inventory_row_by_id(pk)
        if not data:
            raise NotFound
        result = marshal(data, fields_item_inventory_cn, envelope=structure_key_item_cn)
        return jsonify(result)

    def delete(self, pk):
        """
        Example:
            curl http://0.0.0.0:5000/yonyou/inventory/1 -X DELETE
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


class InventoryListResource(Resource):
    """
    InventoryListResource
    """
    decorators = [token_auth.login_required]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:5000/yonyou/inventories
            curl http://0.0.0.0:5000/yonyou/inventories?last_pk=1000&limit_num=2
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('last_pk', type=int, default=0, location='args')
        filter_parser.add_argument('limit_num', type=int, default=20, location='args')

        filter_parser_args = filter_parser.parse_args()

        # data = get_inventory_rows()
        data = get_inventory_limit_rows_by_last_id(**filter_parser_args)

        result = marshal(data, fields_item_inventory, envelope=structure_key_items_cn)

        # todo 附加名称
        for result_item in result[structure_key_items_cn]:
            enum_items_info = get_enum_items_row_by_id(result_item['brand_id'])
            result_item['brand_name'] = enum_items_info.Name if enum_items_info else None

        return jsonify(result)


class InventoryPaginationResource(Resource):
    """
    InventoryPaginationResource
    """
    decorators = [token_auth.login_required]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:5000/yonyou/inventories/pagination
            curl http://0.0.0.0:5000/yonyou/inventories/pagination?page=2000&per_page=2
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('page', type=int, default=1, location='args')
        filter_parser.add_argument('per_page', type=int, default=20, location='args')

        filter_parser_args = filter_parser.parse_args()

        pagination_obj = get_inventory_pagination(**filter_parser_args)

        result = marshal(pagination_obj.items, fields_item_inventory, envelope=structure_key_items)
        result['total'] = pagination_obj.total
        return jsonify(result)


class InventoryListSyncResource(Resource):
    """
    InventoryListSyncResource
    """
    decorators = [token_auth.login_required]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:5000/yonyou/inventories/sync
        :return:
        """
        last_pk = 0
        limit_num = 2000

        count_duplicate = 0

        while 1:
            inventory_rows = get_inventory_limit_rows_by_last_id(last_pk=last_pk, limit_num=limit_num)
            if not inventory_rows:
                break
            for inventory_item in inventory_rows:

                last_pk = inventory_item.id

                # 获取品牌
                production_brand = ''
                if inventory_item.productInfo:
                    enum_items_info = get_enum_items_row_by_id(inventory_item.productInfo)
                    production_brand = enum_items_info.Name.strip() if enum_items_info else ''

                production_model = inventory_item.specification.strip()

                # 判断重复
                count_dup = count_production(production_brand=production_brand, production_model=production_model)
                if count_dup:
                    count_duplicate += 1
                    print(production_brand, production_model)
                    print(count_duplicate)
                    continue
                current_time = datetime.utcnow()
                production_data = {
                    'production_brand': production_brand,
                    'production_model': inventory_item.specification,
                    'note': inventory_item.name,
                    'create_time': current_time,
                    'update_time': current_time,
                }
                add_production(production_data)

        result = {
            '总数': count_inventory(),
            '过滤重复': count_duplicate,
            '成功导入': count_production(),
        }

        return jsonify(result)
