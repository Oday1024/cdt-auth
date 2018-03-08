#!/usr/local/bin/venv/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/5 16:36
# @Author  : ShenFeng
# @Site    : 
# @File    : models.py
# @Software: PyCharm


from datetime import datetime
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
# 使用Flask-Login扩展来实现用户登录
# UserMixin实现了Flask-Login扩展要求Users模型必须实现的方法
# Users模型必须继承UserMixin，当然也可以自己写实现方法
# 详见http://docs.jinkan.org/docs/flask-login/#id6
from flask_login import UserMixin, AnonymousUserMixin


# 用户表
class Users(UserMixin, db.Model):
    # 数据库名称
    __tablename__ = 'td_user'
    # 数据库schema
    __table_args__ = {
        'schema': 'sys'
    }
    id = db.Column(db.Integer, primary_key=True)
    open_id = db.Column(db.String(128), nullable=False)
    account = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    deleted = db.Column(db.Integer, default=0)
    b_inside = db.Column(db.Integer, default=0)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)
    updater = db.Column(db.String(128))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    creater = db.Column(db.String(128))
    data_role = db.Column(db.String(128))
    data_access_level = db.Column(db.Integer, default=0)
    inside_default_role_id = db.Column(db.String(128))

    # 设置明文密码为不可读
    @property
    def passwd(self):
        raise AttributeError(u'密码已经被hash，不可读取！')

    # 定义修改密码方法
    @passwd.setter
    def passwd(self, passwd):
        self.password = generate_password_hash(passwd)

    # 对密码进行验证
    def verify_password(self, passwd):
        return check_password_hash(self.password, passwd)

    # # 初始化Users类，并且设置默认用户和默认权限
    # def __init__(self, account, passwd, open_id):
    #     self.account = account
    #     self.password = self.passwd.setter(passwd)
    #     self.open_id = open_id


# 角色表
class Roles(db.Model):
    # 数据库名称
    __tablename__ = 'td_role'
    # 数据库schema
    __table_args__ = {
        'schema': 'sys'
    }
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.String(128))
    role_name = db.Column(db.String(128))
    data_scope = db.Column(db.Integer, default=0)
    deleted = db.Column(db.Integer, default=0)
    b_inside = db.Column(db.Integer, default=0)
    b_super = db.Column(db.Integer, default=0)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)
    updater = db.Column(db.String(128))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    creater = db.Column(db.String(128))
    data_role = db.Column(db.String(128))
    data_access_level = db.Column(db.Integer, default=0)
    inside_default_open_id = db.Column(db.String(128))

    # 初始化数据库，可以不定义初始化函数
    # SQLAlchemy自动接收所有定义字段为初始化接收参数
    # def __init__(self, role_name):
    #     self.role_name = role_name


# api资源表
class Resources(db.Model):
    # 数据库名称
    __tablename__ = 'td_res'
    # 数据库schema
    __table_args__ = {
        'schema': 'sys'
    }
    id = db.Column(db.Integer, primary_key=True)
    res_id = db.Column(db.String(128))
    res_name = db.Column(db.String(128))
    func_name = db.Column(db.String(128))
    res_flag = db.Column(db.String(128))
    res_path = db.Column(db.String(128))
    res_type_id = db.Column(db.Integer)
    res_type = db.Column(db.String(128))
    p_res_id = db.Column(db.String(128))
    p_res_name = db.Column(db.String(128))
    api_url = db.Column(db.String(128))
    sys_res_id = db.Column(db.String(128))
    sys_res_name = db.Column(db.String(128))
    sys_name = db.Column(db.String(128))
    sys_flag = db.Column(db.String(128))
    deleted = db.Column(db.Integer, default=0)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)
    updater = db.Column(db.String(128))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    creater = db.Column(db.String(128))
    data_access_level = db.Column(db.Integer, default=0)


# 用户角色关联表
class RoleUser(db.Model):
    # 数据库名称
    __tablename__ = 'td_role_user'
    # 数据库schema
    __table_args__ = {
        'schema': 'sys'
    }
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.String(128))
    open_id = db.Column(db.String(128))
    deleted = db.Column(db.Integer, default=0)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)
    updater = db.Column(db.String(128))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    creater = db.Column(db.String(128))
    data_role = db.Column(db.String(128))
    data_access_level = db.Column(db.Integer, default=0)


# 角色资源关联表
class RoleResource(db.Model):
    # 数据库名称
    __tablename__ = 'td_role_res'
    # 数据库schema
    __table_args__ = {
        'schema': 'sys'
    }
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.String(128))
    res_id = db.Column(db.String(128))
    deleted = db.Column(db.Integer, default=0)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)
    updater = db.Column(db.String(128))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    creater = db.Column(db.String(128))
    data_role = db.Column(db.String(128))
    data_access_level = db.Column(db.Integer, default=0)


# 日志表
class Log(db.Model):
    # 数据库名称
    __tablename__ = 'td_log'
    # 数据库schema
    __table_args__ = {
        'schema': 'sys'
    }
    id = db.Column(db.Integer, primary_key=True)
    log_time = db.Column(db.DateTime, default=datetime.utcnow)
    account = db.Column(db.String(128))
    res_id = db.Column(db.String(128))
    res_path = db.Column(db.String(128))
    sys_res_id = db.Column(db.String(128))
    sys_res_name = db.Column(db.String(128))
    sys_res_path = db.Column(db.String(128))
    page_res_id = db.Column(db.String(128))
    page_res_name = db.Column(db.String(128))
    page_res_path = db.Column(db.String(128))
    func_res_id = db.Column(db.String(128))
    func_res_name = db.Column(db.String(128))
    func_res_path = db.Column(db.String(128))
    params = db.Column(db.String(128))
    log_date = db.Column(db.Date)


# 菜单资源表
class Menu(db.Model):
    # 数据库名称
    __tablename__ = 'td_menu'
    # 数据库schema
    __table_args__ = {
        'schema': 'sys'
    }
    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.String(128))
    menu_name = db.Column(db.String(128))
    menu_res_path = db.Column(db.String(128))
    p_menu_id = db.Column(db.String(128))
    sys_res_id = db.Column(db.String(128))
    sys_res_name = db.Column(db.String(128))
    sys_res_path = db.Column(db.String(128))
    page_res_id = db.Column(db.String(128))
    page_res_name = db.Column(db.String(128))
    page_res_path = db.Column(db.String(128))
    sort_id = db.Column(db.Integer)
    icon = db.Column(db.String(128))
    deleted = db.Column(db.Integer, default=0)


# 资源类型
class ResType(db.Model):
    # 数据库名称
    __tablename__ = 'td_res_type'
    # 数据库schema
    __table_args__ = {
        'schema': 'sys'
    }
    id = db.Column(db.Integer, primary_key=True)
    res_type = db.Column(db.String(128), unique=True)
    deleted = db.Column(db.Integer, default=0)


