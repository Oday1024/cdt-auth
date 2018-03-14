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
from flask_login import LoginManager
from config import config


# 构造应用模块实例
bootstrap = Bootstrap()
db = SQLAlchemy()


# 使用Flask-Login扩展来实现用户登录；
# login_manager构造函数
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'api_1_0.login'


# 创建应用方法
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # 初始化应用模块实例
    bootstrap.init_app(app)
    db.init_app(app)

    # 创建app时初始化login_manager
    login_manager.init_app(app)


    # 注册用户认证蓝图
    from .api_1_0 import sysapi as sysapi_blueprint
    app.register_blueprint(sysapi_blueprint)

    return app
