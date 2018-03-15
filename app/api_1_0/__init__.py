#!/usr/local/bin/venv/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 17:23
# @Author  : ShenFeng
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm


from flask import Blueprint
from flask_restful import Api
from .auth import Login
from .usermgr import UserList
from .common import RoleList


# 创建sysapi蓝图
sysapi = Blueprint('sysapi', __name__, url_prefix='/authsys/api')
# 创建Api的实例
api = Api(sysapi)


"""添加所有api资源"""
# 注册资源
api.add_resource(Login, '/account/login')
api.add_resource(RoleList, '/resource/rolelist')
api.add_resource(UserList, '/usermgr/getuserlist')

