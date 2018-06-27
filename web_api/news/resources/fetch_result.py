#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: fetch_result.py
@time: 2018-05-30 19:34
"""


from __future__ import unicode_literals

from flask import jsonify, make_response
from flask_restful import Resource, marshal, reqparse

from web_api.news.outputs.fetch_result import fields_item
from web_api.news.reqparsers.fetch_result import (
    request_parser,
    request_parser_item_post,
    request_parser_item_put,
    structure_key_item,
    structure_key_items,
)
from web_api.commons.exceptions import BadRequest, NotFound
from web_api.news.apis.fetch_result import (
    get_fetch_result_row_by_id,
    edit_fetch_result,
    delete_fetch_result,
    get_fetch_result_limit_rows_by_last_id,
    add_fetch_result,
    get_fetch_result_pagination,
)
from web_api.commons.http_token_auth import token_auth
from web_api import app

SUCCESS_MSG = app.config['SUCCESS_MSG']
FAILURE_MSG = app.config['FAILURE_MSG']


class FetchResultResource(Resource):
    """
    FetchResultResource
    """
    decorators = [token_auth.login_required]

    def get(self, pk):
        """
        Example:
            curl http://0.0.0.0:5000/news/fetch_result/1
        :param pk:
        :return:
        """
        data = get_fetch_result_row_by_id(pk)
        if not data:
            raise NotFound
        result = marshal(data, fields_item, envelope=structure_key_item)
        return jsonify(result)

    def delete(self, pk):
        """
        Example:
            curl http://0.0.0.0:5000/news/fetch_result/1 -X DELETE
        :param pk:
        :return:
        """
        result = delete_fetch_result(pk)
        if result:
            success_msg = SUCCESS_MSG.copy()
            return make_response(jsonify(success_msg), 204)
        else:
            failure_msg = FAILURE_MSG.copy()
            return make_response(jsonify(failure_msg), 400)

    def put(self, pk):
        """
        Example:
            curl http://0.0.0.0:5000/news/fetch_result/1001 -H "Content-Type: application/json" -X PUT -d '
            {
                "fetch_result": {
                    "task_id": 14,
                    "platform_id": 3,
                    "platform_name": "头条_put",
                    "channel_id": 0,
                    "channel_name": "",
                    "article_id": "6527896212211761677",
                    "article_url": "https://www.toutiao.com/i6527896212211761677/",
                    "article_title": "【交易机会】澳美短线或继续回调，中长线仍旧看多",
                    "article_author_id": "69781315016",
                    "article_author_name": "恒信贵金属",
                    "article_tags": "外汇,经济,贵金属,斐波那契,投资",
                    "article_abstract": "本周，在新任美联储主席鲍威尔国会首秀发表鹰派言论之后，近期在90下方苦苦挣扎的美元指数迅速上涨并且一举突破90阻力。",
                    "article_content": "<div><p>本周，在新任美联储主席鲍威尔国会首秀发表鹰派言论之后，近期在90下方苦苦挣扎的美元指数迅速上涨并且一举突破90阻力。但是需要注意的是，美元靓丽的表现可能只是短期的超跌反弹而已，中长线美元依旧缺乏上涨的动力。因为此前市场普遍预期美联储在2018年全年会实现三次加息，某些观点激进的机构甚至认为可能会达到4-5次。</p><p><img src=\"http://p3.pstatp.com/large/66c30000919fda0c1200\" img_width=\"1280\" img_height=\"849\" alt=\"【交易机会】澳美短线或继续回调，中长线仍旧看多\" inline=\"0\"></p><p>在这样的背景下，加息的如期进行或许很难再点燃市场的热情。美元指数虽然短线会有反弹，但中长期大概率仍将是挣扎的走势。</p><p><img src=\"http://p1.pstatp.com/large/66c10001bf8b706efaf1\" img_width=\"554\" img_height=\"327\" alt=\"【交易机会】澳美短线或继续回调，中长线仍旧看多\" inline=\"0\"></p><p>从美元指数周线图来看，目前已经跌破了从2015年以来形成的头部区域，呈现明显的下跌走势，或许短线有抄底反弹的可能，但是不改中长期的弱势。</p><p>对于澳元兑美元来讲，我们维持长期看涨的观点。澳洲经济将受益于全球经济的复苏尤其是中国在大宗商品需求上的增长，澳元也仍将受益于这轮美元弱势、非美强势的大环境。</p><p><img src=\"http://p1.pstatp.com/large/66c30000901f1c3a4f5e\" img_width=\"554\" img_height=\"235\" alt=\"【交易机会】澳美短线或继续回调，中长线仍旧看多\" inline=\"0\"></p><p>从日线图上来看，澳元兑美元在触及0.8130重要阻力后开始回调，将可能测试斐波那契回调线38.2%的支撑0.7630和自2016年以来形成的上升趋势线的支撑，若这两个支撑区域未被突破可以此为依托做多。</p><p>感谢关注，恒信贵金属！</p></div>",
                    "article_pub_time": "2018-03-01 16:51:16",
                    "create_time": "2018-05-18 10:10:03",
                    "update_time": "2018-05-18 10:10:03"
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
        result = edit_fetch_result(pk, request_data)
        if result:
            success_msg = SUCCESS_MSG.copy()
            return make_response(jsonify(success_msg), 200)
        else:
            failure_msg = FAILURE_MSG.copy()
            return make_response(jsonify(failure_msg), 400)


class FetchResultListResource(Resource):
    """
    FetchResultListResource
    """
    decorators = [token_auth.login_required]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:5000/news/fetch_results
            curl http://0.0.0.0:5000/news/fetch_results?last_pk=1000&limit_num=2
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('last_pk', type=int, default=0, location='args')
        filter_parser.add_argument('limit_num', type=int, default=20, location='args')

        filter_parser_args = filter_parser.parse_args()

        # data = get_fetch_result_rows()
        data = get_fetch_result_limit_rows_by_last_id(**filter_parser_args)
        result = marshal(data, fields_item, envelope=structure_key_items)
        return jsonify(result)

    def post(self):
        """
        Example:
            curl http://0.0.0.0:5000/news/fetch_results -H "Content-Type: application/json" -X POST -d '
            {
                "fetch_result": {
                    "task_id": 14,
                    "platform_id": 3,
                    "platform_name": "头条_post",
                    "channel_id": 0,
                    "channel_name": "",
                    "article_id": "6527896212211761677",
                    "article_url": "https://www.toutiao.com/i6527896212211761677/",
                    "article_title": "【交易机会】澳美短线或继续回调，中长线仍旧看多",
                    "article_author_id": "69781315016",
                    "article_author_name": "恒信贵金属",
                    "article_tags": "外汇,经济,贵金属,斐波那契,投资",
                    "article_abstract": "本周，在新任美联储主席鲍威尔国会首秀发表鹰派言论之后，近期在90下方苦苦挣扎的美元指数迅速上涨并且一举突破90阻力。",
                    "article_content": "<div><p>本周，在新任美联储主席鲍威尔国会首秀发表鹰派言论之后，近期在90下方苦苦挣扎的美元指数迅速上涨并且一举突破90阻力。但是需要注意的是，美元靓丽的表现可能只是短期的超跌反弹而已，中长线美元依旧缺乏上涨的动力。因为此前市场普遍预期美联储在2018年全年会实现三次加息，某些观点激进的机构甚至认为可能会达到4-5次。</p><p><img src=\"http://p3.pstatp.com/large/66c30000919fda0c1200\" img_width=\"1280\" img_height=\"849\" alt=\"【交易机会】澳美短线或继续回调，中长线仍旧看多\" inline=\"0\"></p><p>在这样的背景下，加息的如期进行或许很难再点燃市场的热情。美元指数虽然短线会有反弹，但中长期大概率仍将是挣扎的走势。</p><p><img src=\"http://p1.pstatp.com/large/66c10001bf8b706efaf1\" img_width=\"554\" img_height=\"327\" alt=\"【交易机会】澳美短线或继续回调，中长线仍旧看多\" inline=\"0\"></p><p>从美元指数周线图来看，目前已经跌破了从2015年以来形成的头部区域，呈现明显的下跌走势，或许短线有抄底反弹的可能，但是不改中长期的弱势。</p><p>对于澳元兑美元来讲，我们维持长期看涨的观点。澳洲经济将受益于全球经济的复苏尤其是中国在大宗商品需求上的增长，澳元也仍将受益于这轮美元弱势、非美强势的大环境。</p><p><img src=\"http://p1.pstatp.com/large/66c30000901f1c3a4f5e\" img_width=\"554\" img_height=\"235\" alt=\"【交易机会】澳美短线或继续回调，中长线仍旧看多\" inline=\"0\"></p><p>从日线图上来看，澳元兑美元在触及0.8130重要阻力后开始回调，将可能测试斐波那契回调线38.2%的支撑0.7630和自2016年以来形成的上升趋势线的支撑，若这两个支撑区域未被突破可以此为依托做多。</p><p>感谢关注，恒信贵金属！</p></div>",
                    "article_pub_time": "2018-03-01 16:51:16",
                    "create_time": "2018-05-18 10:10:03",
                    "update_time": "2018-05-18 10:10:03"
                }
            }'
        :return:
        """

        request_args = request_parser.parse_args()
        request_item_args = request_parser_item_post.parse_args(req=request_args)
        if not request_item_args:
            raise BadRequest('Bad request.')

        request_data = request_item_args
        result = add_fetch_result(request_data)
        if result:
            success_msg = SUCCESS_MSG.copy()
            success_msg['id'] = result
            return make_response(jsonify(success_msg), 201)
        else:
            failure_msg = FAILURE_MSG.copy()
            return make_response(jsonify(failure_msg), 400)


class FetchResultPaginationResource(Resource):
    """
    FetchResultPaginationResource
    """
    decorators = [token_auth.login_required]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:5000/news/fetch_results/pagination
            curl http://0.0.0.0:5000/news/fetch_results/pagination?page=2000&per_page=2
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('page', type=int, default=1, location='args')
        filter_parser.add_argument('per_page', type=int, default=20, location='args')

        filter_parser_args = filter_parser.parse_args()

        pagination_obj = get_fetch_result_pagination(**filter_parser_args)

        result = marshal(pagination_obj.items, fields_item, envelope=structure_key_items)
        result['total'] = pagination_obj.total
        return jsonify(result)
