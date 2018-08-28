#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: current_stock.py
@time: 2018-08-23 14:17
"""


from libs.mysql_orm_op import DbInstance
from web_api.databases.yonyou import db
from web_api.models.yonyou import STCurrentStock

db_instance = DbInstance(db)


def get_current_stock_row_by_id(current_stock_id):
    """
    通过 id 获取信息
    :param current_stock_id:
    :return: None/object
    """
    return db_instance.get_row_by_id(STCurrentStock, current_stock_id)


def get_current_stock_row(*args, **kwargs):
    """
    获取信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return db_instance.get_row(STCurrentStock, *args, **kwargs)


def get_current_stock_rows(*args, **kwargs):
    """
    获取列表
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.get_rows(STCurrentStock, *args, **kwargs)


def get_current_stock_limit_rows_by_last_id(last_pk, limit_num, *args, **kwargs):
    """
    通过最后一个主键 id 获取最新信息列表
    :param last_pk:
    :param limit_num:
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.get_limit_rows_by_last_id(STCurrentStock, last_pk, limit_num, *args, **kwargs)


def add_current_stock(current_stock_data):
    """
    添加信息
    :param current_stock_data:
    :return: None/Value of user.id
    :except:
    """
    return db_instance.add(STCurrentStock, current_stock_data)


def edit_current_stock(current_stock_id, current_stock_data):
    """
    修改信息
    :param current_stock_id:
    :param current_stock_data:
    :return: Number of affected rows (Example: 0/1)
    :except:
    """
    return db_instance.edit(STCurrentStock, current_stock_id, current_stock_data)


def delete_current_stock(current_stock_id):
    """
    删除信息
    :param current_stock_id:
    :return: Number of affected rows (Example: 0/1)
    :except:
    """
    return db_instance.delete(STCurrentStock, current_stock_id)


def get_current_stock_pagination(page=1, per_page=10, *args, **kwargs):
    """
    获取列表（分页）
    Usage:
        items: 信息列表
        has_next: 如果本页之后还有超过一个分页，则返回True
        has_prev: 如果本页之前还有超过一个分页，则返回True
        next_num: 返回下一页的页码
        prev_num: 返回上一页的页码
        iter_pages(): 页码列表
        iter_pages(left_edge=2, left_current=2, right_current=5, right_edge=2) 页码列表默认参数
    :param page:
    :param per_page:
    :param args:
    :param kwargs:
    :return:
    """
    rows = db_instance.get_pagination(STCurrentStock, page, per_page, *args, **kwargs)
    return rows


def delete_current_stock_table():
    """
    清空表
    :return:
    """
    return db_instance.delete_table(STCurrentStock)


def count_current_stock(*args, **kwargs):
    """
    计数
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.count(STCurrentStock, *args, **kwargs)
