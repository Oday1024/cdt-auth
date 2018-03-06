#!/usr/local/bin/venv/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/5 16:36
# @Author  : ShenFeng
# @Site    : 
# @File    : models.py
# @Software: PyCharm


from datetime import datetime
from . import db


# 用户表
class Users(db.Model):
    # 数据库名称
    __tablename__ = 'td_user'
    # 数据库schema
    __table_args__ = {
        'schema': 'sys'
    }
    id = db.Column(db.Integer, primary_key=True)
    open_id = db.Column(db.String(32), unique=True)
    account = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    deleted = db.Column(db.Boolean, default=False)
    b_inside = db.Column(db.Boolean, default=False)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)
    updater = db.Column(db.Text())
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    creater = db.Column(db.Text())
    data_role = db.Column(db.Text())
    data_access_level = db.Column(db.Integer, default=0)
    inside_default_role_id = db.Column(db.String(50), )


# 角色表
class Roles(db.Model):
    # 数据库名称
    __tablename__ = 'td_role'
    # 数据库schema
    __table_args__ = {
        'schema': 'sys'
    }
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.String(32), unique=True)
    role_name = db.Column(db.String(64), unique=True)
    data_scope = db.Column(db.Boolean, default=False)
    deleted = db.Column(db.Boolean, default=False)
    b_inside = db.Column(db.Boolean, default=False)
    b_super = db.Column(db.Boolean, default=False)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)
    updater = db.Column(db.Text())
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    creater = db.Column(db.Text())
    data_role = db.Column(db.Text())
    data_access_level = db.Column(db.Integer, default=0)
    inside_default_open_id = db.Column(db.String(50), )


# api资源表
class Resources(db.Model):
    # 数据库名称
    __tablename__ = 'td_res'
    # 数据库schema
    __table_args__ = {
        'schema': 'sys'
    }
    id = db.Column(db.Integer, primary_key=True)
    res_id = db.Column(db.String(32), unique=True)
    res_name = db.Column(db.String(64), unique=True)
    func_name = db.Column(db.String(64))
    res_flag = db.Column(db.String(64))
    res_path = db.Column(db.String(64))
    res_type_id = db.Column(db.Integer)
    res_type = db.Column(db.String(64))
    p_res_id = db.Column(db.String(64))
    p_res_name = db.Column(db.String(64))
    api_url = db.Column(db.String(128))
    sys_res_id = db.Column(db.String(64))
    sys_res_name = db.Column(db.String(64))
    sys_name = db.Column(db.String(64))
    sys_flag = db.Column(db.String(64))
    deleted = db.Column(db.Boolean, default=False)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)
    updater = db.Column(db.Text())
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    creater = db.Column(db.Text())
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
    role_id = db.Column(db.String(32), unique=True)
    open_id = db.Column(db.String(32), unique=True)
    deleted = db.Column(db.Boolean, default=False)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)
    updater = db.Column(db.Text())
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    creater = db.Column(db.Text())
    data_role = db.Column(db.Text())
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
    role_id = db.Column(db.String(32), unique=True)
    res_id = db.Column(db.String(32), unique=True)
    deleted = db.Column(db.Boolean, default=False)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)
    updater = db.Column(db.Text())
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    creater = db.Column(db.Text())
    data_role = db.Column(db.Text())
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
    account = db.Column(db.String(64), unique=True)
    res_id = db.Column(db.String(32), unique=True)
    res_path = db.Column(db.String(64))
    sys_res_id = db.Column(db.String(64))
    sys_res_name = db.Column(db.String(64))
    sys_res_path = db.Column(db.String(64))
    page_res_id = db.Column(db.String(64))
    page_res_name = db.Column(db.String(64))
    page_res_path = db.Column(db.String(64))
    func_res_id = db.Column(db.String(64))
    func_res_name = db.Column(db.String(64))
    func_res_path = db.Column(db.String(64))
    params = db.Column(db.String(256))
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
    menu_id = db.Column(db.String(64), unique=True)
    menu_name = db.Column(db.String(64), unique=True)
    menu_res_path = db.Column(db.String(64), unique=True)
    p_menu_id = db.Column(db.String(64))
    sys_res_id = db.Column(db.String(64))
    sys_res_name = db.Column(db.String(64))
    sys_res_path = db.Column(db.String(64))
    page_res_id = db.Column(db.String(64))
    page_res_name = db.Column(db.String(64))
    page_res_path = db.Column(db.String(64))
    sort_id = db.Column(db.Integer)
    icon = db.Column(db.String(256))
    deleted = db.Column(db.Boolean, default=False)


# 资源类型
class ResType(db.Model):
    # 数据库名称
    __tablename__ = 'td_res_type'
    # 数据库schema
    __table_args__ = {
        'schema': 'sys'
    }
    id = db.Column(db.Integer, primary_key=True)
    res_type = db.Column(db.String(64), unique=True)
    deleted = db.Column(db.Boolean, default=False)