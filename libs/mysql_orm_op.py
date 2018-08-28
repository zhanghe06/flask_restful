#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: mysql_orm_op.py
@time: 2018-05-30 21:42
"""


from sqlalchemy.inspection import inspect
from sqlalchemy import distinct


class DbInstance(object):
    def __init__(self, db_instance):
        self.db_instance = db_instance

    # todo get_rows order_by
    # todo insert ignore

    def get_row_by_id(self, model_class, pk_id):
        """
        通过 id 获取信息
        :param model_class:
        :param pk_id:
        :return: None/object
        """
        return self.db_instance.session.query(model_class).get(pk_id)

    def get_row(self, model_class, *args, **kwargs):
        """
        获取信息
        Usage:
            # 方式一
            get_row(User, User.id > 1)
            # 方式二
            test_condition = {
                'name': "Larry"
            }
            get_row(User, **test_condition)
        :param model_class:
        :param args:
        :param kwargs:
        :return: None/object
        """
        return self.db_instance.session \
            .query(model_class) \
            .filter(*args) \
            .filter_by(**kwargs) \
            .first()

    def get_rows(self, model_class, *args, **kwargs):
        """
        获取列表信息
        Usage:
            # 方式一
            get_lists(User, User.id > 1)
            # 方式二
            test_condition = {
                'name': "Larry"
            }
            get_lists(User, **test_condition)
        :param model_class:
        :param args:
        :param kwargs:
        :return: None/list
        """
        return self.db_instance.session \
            .query(model_class) \
            .filter(*args) \
            .filter_by(**kwargs) \
            .all()

    def get_rows_by_ids(self, model_class, pk_ids):
        """
        通过一组 ids 获取信息列表
        :param model_class:
        :param pk_ids:
        :return: list
        """
        model_pk = inspect(model_class).primary_key[0]
        return self.db_instance.session \
            .query(model_class) \
            .filter(model_pk.in_(pk_ids)) \
            .all()

    def get_limit_rows_by_last_id(self, model_class, last_pk, limit_num, *args, **kwargs):
        """
        通过最后一个主键 id 获取最新信息列表
        避免id乱序, 需要加入order_by
        适用场景：
        1、动态加载
        2、快速定位
        :param model_class:
        :param last_pk:
        :param limit_num:
        :param args:
        :param kwargs:
        :return: list
        """
        model_pk = inspect(model_class).primary_key[0]
        return self.db_instance.session \
            .query(model_class) \
            .filter(model_pk > last_pk, *args) \
            .filter_by(**kwargs) \
            .order_by(model_pk) \
            .limit(limit_num) \
            .all()

    def count(self, model_class, *args, **kwargs):
        """
        计数
        Usage:
            # 方式一
            count(User, User.id > 1)
            # 方式二
            test_condition = {
                'name': "Larry"
            }
            count(User, **test_condition)
        :param model_class:
        :param args:
        :param kwargs:
        :return: 0/Number（int）
        """
        return self.db_instance.session \
            .query(model_class) \
            .filter(*args) \
            .filter_by(**kwargs) \
            .count()

    def add(self, model_class, data):
        """
        添加信息
        :param model_class:
        :param data:
        :return: None/Value of model_obj.PK
        """
        model_obj = model_class(**data)
        try:
            self.db_instance.session.add(model_obj)
            self.db_instance.session.commit()
            return inspect(model_obj).identity[0]
        except Exception as e:
            self.db_instance.session.rollback()
            raise e

    def edit(self, model_class, pk_id, data):
        """
        修改信息
        :param model_class:
        :param pk_id:
        :param data:
        :return: Number of affected rows (Example: 0/1)
        """
        model_pk_name = inspect(model_class).primary_key[0].name
        model_pk = getattr(model_class, model_pk_name)
        try:
            model_obj = self.db_instance.session.query(model_class).filter(model_pk == pk_id)
            result = model_obj.update(data)
            self.db_instance.session.commit()
            return result
        except Exception as e:
            self.db_instance.session.rollback()
            raise e

    def merge(self, model_class, data):
        """
        覆盖信息(没有新增，存在更新)
        数据中必须带主键字段
        :param model_class:
        :param data:
        :return: Value of PK
        """
        model_obj = model_class(**data)
        try:
            r = self.db_instance.session.merge(model_obj)
            self.db_instance.session.commit()
            return inspect(r).identity[0]
        except Exception as e:
            self.db_instance.session.rollback()
            raise e

    def increase(self, model_class, pk_id, field, num=1, **kwargs):
        """
        字段自增
        :param model_class:
        :param pk_id:
        :param field:
        :param num:
        :param kwargs:
        :return: Number of affected rows (Example: 0/1)
        """
        model_pk_name = inspect(model_class).primary_key[0].name
        model_pk = getattr(model_class, model_pk_name)
        try:
            model_obj = self.db_instance.session.query(model_class).filter(model_pk == pk_id)
            value = getattr(model_class, field) + num
            data = {
                field: value
            }
            data.update(**kwargs)  # 更新扩展字段
            result = model_obj.update(data)
            self.db_instance.session.commit()
            return result
        except Exception as e:
            self.db_instance.session.rollback()
            raise e

    def delete(self, model_class, pk_id):
        """
        删除信息
        :param model_class:
        :param pk_id:
        :return: Number of affected rows (Example: 0/1)
        """
        model_pk_name = inspect(model_class).primary_key[0].name
        model_pk = getattr(model_class, model_pk_name)
        try:
            model_obj = self.db_instance.session.query(model_class).filter(model_pk == pk_id)
            result = model_obj.delete()
            self.db_instance.session.commit()
            return result
        except Exception as e:
            self.db_instance.session.rollback()
            raise e

    def get_distinct_field(self, model_class, field, *args, **kwargs):
        try:
            return self.db_instance.session \
                .query(distinct(getattr(model_class, field)).label(field)) \
                .filter(*args) \
                .filter_by(**kwargs) \
                .all()
        except Exception as e:
            self.db_instance.session.rollback()
            raise e

    @staticmethod
    def get_pagination(model_class, page=1, per_page=10, *args, **kwargs):
        """
        获取信息列表（分页）
        Usage:
            items: 信息列表
            has_next: 如果本页之后还有超过一个分页，则返回True
            has_prev: 如果本页之前还有超过一个分页，则返回True
            next_num: 返回下一页的页码
            prev_num: 返回上一页的页码
            iter_pages(): 页码列表
            iter_pages(left_edge=2, left_current=2, right_current=5, right_edge=2) 页码列表默认参数
        :param model_class:
        :param page:
        :param per_page:
        :param args:
        :param kwargs:
        :return: None/object
        """
        return model_class.query \
            .filter(*args) \
            .filter_by(**kwargs) \
            .order_by(inspect(model_class).primary_key[0].desc()) \
            .paginate(page, per_page, False, 100)

    def delete_table(self, model_class):
        """
        清空表（保留结构）
        :param model_class:
        :return:
        """
        try:
            model_obj = self.db_instance.session.query(model_class)
            result = model_obj.delete()
            self.db_instance.session.commit()
            return result
        except Exception as e:
            self.db_instance.session.rollback()
            raise e

    def drop_table(self, model_class):
        """
        删除表（数据、结构全部清除）
        :param model_class:
        :return:
        """
        return model_class.__table__.drop(bind=self.db_instance.engine)

    def insert_rows(self, model_class, data_list):
        """
        批量插入数据（遇到主键/唯一索引重复，忽略报错，继续执行下一条插入任务）
        注意：
        Warning: Duplicate entry
        警告有可能会提示：
        UnicodeEncodeError: 'ascii' codec can't encode characters in position 17-20: ordinal not in range(128)
        处理：
        import sys

        reload(sys)
        sys.setdefaultencoding('utf8')

        sql 语句大小限制
        show VARIABLES like '%max_allowed_packet%';
        参考：http://dev.mysql.com/doc/refman/5.7/en/packet-too-large.html

        :param model_class:
        :param data_list:
        :return:
        """
        try:
            result = self.db_instance.session.execute(model_class.__table__.insert().prefix_with('IGNORE'), data_list)
            self.db_instance.session.commit()
            return result.rowcount
        except Exception as e:
            self.db_instance.session.rollback()
            raise e

    def update_rows(self, model_class, data, *args, **kwargs):
        """
        批量修改数据
        :param model_class:
        :param data:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            model_obj = self.db_instance.session.query(model_class).filter(*args).filter_by(**kwargs)
            result = model_obj.update(data, synchronize_session=False)
            self.db_instance.session.commit()
            return result
        except Exception as e:
            self.db_instance.session.rollback()
            raise e

    def update_rows_by_ids(self, model_class, pk_ids, data):
        """
        根据一组主键id 批量修改数据
        """
        model_pk = inspect(model_class).primary_key[0]
        try:
            model_obj = self.db_instance.session.query(model_class).filter(model_pk.in_(pk_ids))
            result = model_obj.update(data, synchronize_session=False)
            self.db_instance.session.commit()
            return result
        except Exception as e:
            self.db_instance.session.rollback()
            raise e
