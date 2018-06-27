#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: urls.py
@time: 2018-05-31 17:55
"""

from web_api.news import news_api
from web_api.news.resources.fetch_result import (
    FetchResultResource,
    FetchResultListResource,
    FetchResultPaginationResource
)


news_api.add_resource(
    FetchResultResource,
    '/fetch_result/<int:pk>',
    endpoint='fetch_result',
    strict_slashes=False
)

news_api.add_resource(
    FetchResultListResource,
    '/fetch_results',
    endpoint='fetch_results',
    strict_slashes=False
)

news_api.add_resource(
    FetchResultPaginationResource,
    '/fetch_results/pagination',
    endpoint='fetch_results_pagination',
    strict_slashes=False
)
