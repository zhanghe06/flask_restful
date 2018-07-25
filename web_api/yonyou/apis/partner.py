#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: partner.py
@time: 2018-07-24 00:25
"""


from libs.mysql_orm_op import DbInstance
from web_api.databases.yonyou import db
from web_api.models.yonyou import AAPartner

db_instance = DbInstance(db)


def get_partner_row_by_id(partner_id):
    """
    通过 id 获取信息
    :param partner_id:
    :return: None/object
    """
    return db_instance.get_row_by_id(AAPartner, partner_id)


def get_partner_row(*args, **kwargs):
    """
    获取信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return db_instance.get_row(AAPartner, *args, **kwargs)


def get_partner_rows(*args, **kwargs):
    """
    获取列表
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.get_rows(AAPartner, *args, **kwargs)


def get_partner_limit_rows_by_last_id(last_pk, limit_num, *args, **kwargs):
    """
    通过最后一个主键 id 获取最新信息列表
    :param last_pk:
    :param limit_num:
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.get_limit_rows_by_last_id(AAPartner, last_pk, limit_num, *args, **kwargs)


def add_partner(partner_data):
    """
    添加信息
    :param partner_data:
    :return: None/Value of user.id
    :except:
    """
    return db_instance.add(AAPartner, partner_data)


def edit_partner(partner_id, partner_data):
    """
    修改信息
    :param partner_id:
    :param partner_data:
    :return: Number of affected rows (Example: 0/1)
    :except:
    """
    return db_instance.edit(AAPartner, partner_id, partner_data)


def delete_partner(partner_id):
    """
    删除信息
    :param partner_id:
    :return: Number of affected rows (Example: 0/1)
    :except:
    """
    return db_instance.delete(AAPartner, partner_id)


def get_partner_pagination(page=1, per_page=10, *args, **kwargs):
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
    rows = db_instance.get_pagination(AAPartner, page, per_page, *args, **kwargs)
    return rows


def delete_partner_table():
    """
    清空表
    :return:
    """
    return db_instance.delete_table(AAPartner)


def count_partner(*args, **kwargs):
    """
    计数
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.count(AAPartner, *args, **kwargs)
