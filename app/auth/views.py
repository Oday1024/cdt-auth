#!/usr/local/bin/venv/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 22:35
# @Author  : ShenFeng
# @Site    : 
# @File    : views.py
# @Software: PyCharm


from flask import request, jsonify
from flask_login import login_user, logout_user, login_required, \
    current_user
from . import auth
from ..models import Users


# 将登录成功返回数据存储在LOGIN_SUCCESS字典中
LOGIN_SUCCESS = {
    "respcode": "200200",
    "result": "ok"
}


# 将登录失败返回数据存储在LOGIN_ERR字典中
LOGIN_ERR = {
    "respcode": "400400",
    "result": "用户名密码错误"
}


@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()


@auth.route('/authsys/login/', methods=['POST'])
def login():
    """
    1、获取请求参数用户名、密码
    2、验证用户名密码是否正确，如果正确，返回json格式正确响应码
    3、如果用户名或者密码错误，则返回json格式错误码
    :return:
    200200，正确
    400400，错误
    """
    # 获取请求参数中的用户名、密码明文
    # 采用curl -X POST http://127.0.0.1:5000/authsys/login/ -d 'username=guest&password=shenfeng'已经OK
    username = request.form.get('username')
    passwd = request.form.get('password')

    # 测试请求参数数据
    # print(username)
    # print(passwd)
    # print(request.data)

    # 用请求参数中的username查询数据库判断登录用户是否存在
    user = Users.query.filter_by(account=username).first()
    # 如果用户存在并且验证用户密码与数据库hash后的值相等
    if user is not None and user.verify_password(passwd):
        return jsonify(LOGIN_SUCCESS)
    else:
        return jsonify(LOGIN_ERR)
