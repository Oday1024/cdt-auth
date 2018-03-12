#!/usr/local/bin/venv/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/11 22:46
# @Author  : ShenFeng
# @Site    : 
# @File    : views.py
# @Software: PyCharm


#!/usr/local/bin/venv/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 22:35
# @Author  : ShenFeng
# @Site    :
# @File    : views.py
# @Software: PyCharm

#
# import time
# from flask import request, jsonify
# from flask_login import login_required
# from . import resourcemgr
# from ..models import Menu
#
#
# @login_required
# @resourcemgr('/authsys/api/menulist', methods=['GET'])
# def menulist():
#     """
#     获取系统菜单资源，传入sys_res_path代表系统名称，对应td_menu表中page_res_path：
#     1、连接数据库
#     2、查表td_menu（Menu模型）按照page_res_path过滤
#     3、返回过滤结果的json格式
#     """
#     sys_res_path = request.form.get('sys_res_path')
#
#     if sys_res_path == '/authsys':
#         menulist = Menu.query.filter_by(page_res_path='/authsys')
#         return jsonify(menulist)
#     else:
#         return '错误请求'



