#!/usr/local/bin/venv/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 17:23
# @Author  : ShenFeng
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm


from flask import Blueprint
from flask_restful import Api

sysapi = Blueprint('sysapi', __name__)
api = Api(sysapi)

from . import auth, usermgr



