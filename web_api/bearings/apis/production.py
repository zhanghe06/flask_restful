#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: production.py
@time: 2018-08-28 11:23
"""


import datetime

from libs.mysql_orm_op import DbInstance
from web_api.databases.bearings import db
from web_api.models.bearings import Production

db_instance = DbInstance(db)


def get_production_row_by_id(production_id):
    """
    通过 id 获取信息
    :param production_id:
    :return: None/object
    """
    return db_instance.get_row_by_id(Production, production_id)


def get_production_row(*args, **kwargs):
    """
    获取信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return db_instance.get_row(Production, *args, **kwargs)


def get_production_rows(*args, **kwargs):
    """
    获取列表
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.get_rows(Production, *args, **kwargs)


def get_production_limit_rows_by_last_id(last_pk, limit_num, *args, **kwargs):
    """
    通过最后一个主键 id 获取最新信息列表
    :param last_pk:
    :param limit_num:
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.get_limit_rows_by_last_id(Production, last_pk, limit_num, *args, **kwargs)


def add_production(production_data):
    """
    添加信息
    :param production_data:
    :return: None/Value of user.id
    :except:
    """
    return db_instance.add(Production, production_data)


def edit_production(production_id, production_data):
    """
    修改信息
    :param production_id:
    :param production_data:
    :return: Number of affected rows (Example: 0/1)
    :except:
    """
    return db_instance.edit(Production, production_id, production_data)


def delete_production(production_id, force=False):
    """
    删除信息
    :param production_id:
    :param force:
    :return: Number of affected rows (Example: 0/1)
    :except:
    """
    if force:
        return db_instance.delete(Production, production_id)
    else:
        data = {
            'status_delete': True,
            'delete_time': datetime.datetime.utcnow()
        }
        return db_instance.edit(Production, production_id, data)


def get_production_pagination(page=1, per_page=10, *args, **kwargs):
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
    rows = db_instance.get_pagination(Production, page, per_page, *args, **kwargs)
    return rows


def delete_production_table():
    """
    清空表
    :return:
    """
    return db_instance.delete_table(Production)


def count_production(*args, **kwargs):
    """
    计数
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.count(Production, *args, **kwargs)
