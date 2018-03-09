#!/usr/local/bin/venv/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 22:35
# @Author  : ShenFeng
# @Site    : 
# @File    : views.py
# @Software: PyCharm


import time
from flask import request, make_response, jsonify
from flask_login import login_user, logout_user, login_required, \
    current_user
from . import auth
from ..models import Users
from ..util.calljar import getpassword


TOKEN = 'XSRF-TOKEN=eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJhdXRoc3lzIiwic' \
        '3ViIjoie1wiYWNjb3VudFwiOlwic3VwZXJhZG1pblwiLFwib3BlbklkXC' \
        'I6XCI2NGY2YWE0OTllOTFjMTI2YTc0Mjg5MmZiMDNmMzVhZlwiLFwiZGF' \
        '0YUFjY2Vzc0xldmVsXCI6MTB9IiwiaWF0IjoxNTIwNjA4MzU3LCJleHAi' \
        'OjE1MjA2MTAxNTd9.vILwLZtusKsHN5g1bgZJ9kjrsKWSb1pjXdRm9G1nK3E'


# 将登录成功返回数据存储在LOGIN_SUCCESS字典中
LOGIN_SUCCESS = {
    "msg": "200200",
    "result": "true"
}


# 将登录失败返回数据存储在LOGIN_ERR字典中
LOGIN_ERR = {
    "msg": "400400",
    "result": "false"
}


@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()


@auth.route('/authsys/api/account/login', methods=['POST'])
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
    # 采用Restlet Client - REST API Testing 工具测试OK
    username = request.form.get('username')

    # 前端用Date.parse()函数，返回该参数中日期与1970年1月1日午夜之间相差的毫秒数，
    # 因此需要除以1000转换成精确到秒的时间戳格式
    reqkey = request.form.get('key')

    # 精确到秒的时间戳格式，因为是一个int型，不能直接转换成时间格式
    timestamp = int(reqkey) / 1000

    # 1、先将int型的时间戳转换成localtime
    local_time_key = time.localtime(timestamp)

    # 2、再将localtime进行格式化
    key_dt = time.strftime("%Y%m%d %H:%M:%S", local_time_key)

    # print str(key_dt)[0:8]
    # print str(key_dt)[9:17]

    fistkey = 'chuangdada'

    # 取出格式化后的日期，并转化成字符串
    secondkey = str(key_dt)[0:8]

    # 取出格式化后的时分秒，并转化成字符串
    thirdkey = str(key_dt)[9:17]

    passwd = getpassword(request.form.get('password'), fistkey, secondkey, thirdkey)

    # 测试请求参数数据
    # print(username)
    # print(key)
    # print(passwd)

    # 用请求参数中的username查询数据库判断登录用户是否存在
    user = Users.query.filter_by(account=username).first()
    # 如果用户存在并且验证用户密码与数据库hash后的值相等
    if user is not None and user.verify_password(passwd):
        # 构造响应参数
        # make_response的参数不能是dict、数组等，需要先转化为json格式
        rsp = make_response(jsonify(LOGIN_SUCCESS))
        rsp.mimetype = 'application/json'
        # 返回TOKEN值
        rsp.set_cookie(TOKEN)
        return rsp

    else:
        return jsonify(LOGIN_ERR)
