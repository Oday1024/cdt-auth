#!/usr/local/bin/venv/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/5 16:35
# @Author  : ShenFeng
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm


from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config


# 构造应用模块实例
bootstrap = Bootstrap()
db = SQLAlchemy()


# 创建应用方法
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # 初始化应用模块实例
    bootstrap.init_app(app)
    db.init_app(app)

    return app