#!/usr/local/bin/venv/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/5 16:36
# @Author  : ShenFeng
# @Site    : 
# @File    : config.py
# @Software: PyCharm


import os


basedir = os.path.abspath(os.path.dirname(__file__))


# 配置基类
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 开发环境配置
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://authdev:shenfeng@localhost/authdev'


# 测试环境配置
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://authdev:shenfeng@localhost/authdev'


# 生产环境配置
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://auth:shenfeng@localhost/auth'


# 配置字典
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    # 默认配置为开发环境
    'default': DevelopmentConfig
}