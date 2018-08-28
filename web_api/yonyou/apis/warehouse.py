#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: warehouse.py
@time: 2018-08-27 19:20
"""


from libs.mysql_orm_op import DbInstance
from web_api.databases.yonyou import db
from web_api.models.yonyou import AAWarehouse

db_instance = DbInstance(db)


def get_warehouse_row_by_id(warehouse_id):
    """
    通过 id 获取信息
    :param warehouse_id:
    :return: None/object
    """
    return db_instance.get_row_by_id(AAWarehouse, warehouse_id)


def get_warehouse_row(*args, **kwargs):
    """
    获取信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return db_instance.get_row(AAWarehouse, *args, **kwargs)


def get_warehouse_rows(*args, **kwargs):
    """
    获取列表
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.get_rows(AAWarehouse, *args, **kwargs)


def get_warehouse_limit_rows_by_last_id(last_pk, limit_num, *args, **kwargs):
    """
    通过最后一个主键 id 获取最新信息列表
    :param last_pk:
    :param limit_num:
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.get_limit_rows_by_last_id(AAWarehouse, last_pk, limit_num, *args, **kwargs)


def add_warehouse(warehouse_data):
    """
    添加信息
    :param warehouse_data:
    :return: None/Value of user.id
    :except:
    """
    return db_instance.add(AAWarehouse, warehouse_data)


def edit_warehouse(warehouse_id, warehouse_data):
    """
    修改信息
    :param warehouse_id:
    :param warehouse_data:
    :return: Number of affected rows (Example: 0/1)
    :except:
    """
    return db_instance.edit(AAWarehouse, warehouse_id, warehouse_data)


def delete_warehouse(warehouse_id):
    """
    删除信息
    :param warehouse_id:
    :return: Number of affected rows (Example: 0/1)
    :except:
    """
    return db_instance.delete(AAWarehouse, warehouse_id)


def get_warehouse_pagination(page=1, per_page=10, *args, **kwargs):
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
    rows = db_instance.get_pagination(AAWarehouse, page, per_page, *args, **kwargs)
    return rows


def delete_warehouse_table():
    """
    清空表
    :return:
    """
    return db_instance.delete_table(AAWarehouse)


def count_warehouse(*args, **kwargs):
    """
    计数
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.count(AAWarehouse, *args, **kwargs)
