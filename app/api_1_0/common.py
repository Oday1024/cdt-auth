#!/usr/local/bin/venv/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 17:19
# @Author  : ShenFeng
# @Site    : 
# @File    : common.py
# @Software: PyCharm


from flask import jsonify, request
# 采用flask_restful实现接口
from flask_restful import Resource, fields, marshal
from app.models import Roles


"""
定义基础资源数据，如:
1. 角色列表
2. 应用系统资源
3. 功能菜单资源
4. 子功能资源
5. 资源基础数据
6. 资源类型
7. 资源归属
"""

roleList_fields = {
    'role_id': fields.String,
    'role_name': fields.String
}


# 定义响应的json格式生成方法
def return_rolelist_true(data):
    succ = {
        "dataList": data
    }
    return jsonify(succ)


# 角色列表
class RoleList(Resource):
    def get(self):
        roles = Roles.query.all()
        return return_rolelist_true(marshal(roles, roleList_fields))


# 应用系统资源
class SysList(Resource):
    pass

# 功能菜单资源
class MenuList:
    pass


# 子功能资源
class FuncList(Resource):
    pass


# 资源基础数据
class ResList(Resource):
    pass


# 资源类型
class ResType(Resource):
    pass


# 资源归属
class ResBelong(Resource):
    pass