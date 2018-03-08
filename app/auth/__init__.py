#!/usr/local/bin/venv/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/5 16:35
# @Author  : ShenFeng
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm


from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views