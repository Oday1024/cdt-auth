#!/usr/local/bin/venv/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 00:55
# @Author  : ShenFeng
# @Site    : 
# @File    : views.py
# @Software: PyCharm

# 换成flask-restful实现
# from flask import request, jsonify, make_response, json
# from flask_sqlalchemy import Pagination
# from flask_login import login_required
# from . import usermgr
# from app import db
# from app.models import Users, Roles
# from werkzeug.datastructures import MultiDict
#
#
# # def convert_to_json_rolelist(data):
# #     data_list = []  # 需要序列化的列表
# #     for i in data:
# #         tmp = {'id': i[0], 'role_name': i[1]}  # 通过data的每一个元素构造一个字典
# #         data_list.append(tmp)
# #         data_list = json.dumps(data_list, indent=4)
# #     return data_list
# #
# #
# # def convert_to_json_userlist(data):
# #     data_list = []  # 需要序列化的列表
# #     for i in data:
# #         tmp = {'account': i[0], 'open_id': i[1], 'open_id': i[2], 'password': i[3], 'data_role': i[4], 'data_access_level': i[5], 'create_time': i[6]}  # 通过data的每一个元素构造一个字典
# #         data_list.append(tmp)
# #         data_list = json.dumps(data_list, indent=4)
# #     return data_list
#
#
# # # @login_required
# # @usermgr.route('/authsys/api/resource/rolelist', methods=['GET'])
# # def getrolelist():
# #     rolelist = db.session.query(Roles.id, Roles.role_name).all()
# #     print rolelist
# #     return json.dumps(rolelist, default=Users.to_json())
#
# """
# 可以获取到用户列表，但还存在很多问题
# """
# @login_required
# @usermgr.route('/authsys/api/usermgr/getuserlist', methods=['GET'])
# def getuserlist():
#     # 获取请求参数
#     account = request.args.get('account')
#     role_ids = request.args.get('role_ids')
#     current_page = request.args.get('current_page')
#     page_size = request.args.get('page_size')
#
#     # print account
#     # print role_ids
#     # print current_page
#     # print page_size
#     print isinstance(account, MultiDict)
#     print isinstance(role_ids, MultiDict)
#     print isinstance(account, list)
#     print isinstance(role_ids, list)
#
#
#     # if current_page == '1' and page_size == '20':
#     if str(account) is '' and str(role_ids) is '':
#         # 获取用户对象，并且存储为列表
#         userlist = db.session.query(Users.account, Users.open_id, Users.password, Users.data_role,
#                                     Users.data_access_level, Users.create_time).all()
#         # 将列表转化成json格式
#         # 1、先将列表补充上key字段
#         # 2、再讲新的列表转化成字典
#         # 3、用dumps方法讲字典转化为json格式
#         dataList = []
#         userlist_dict = {}
#         for r in userlist:
#             user = {}
#             user['account'] = r[0]
#             user['open_id'] = r[1]
#             user['password'] = r[2]
#             user['data_role'] = r[3]
#             user['data_access_level'] = r[4]
#             user['create_time'] = r[4]
#             dataList.append(user)
#
#         # userlist_dict['dataList'] = 'dataList'
#         userlist_dict['current_page'] = current_page
#         userlist_dict['dataList'] = dataList
#         userlist_dict['page_size'] = page_size
#         userlist_dict['total_results'] = 10
#         userlist_json = json.dumps(userlist_dict)
#
#         # print(userlist_json)
#
#     # users = []
#     # data = {}
#     # for r in results:
#     #     user = {}
#     #     user['id'] = r[0]
#     #     user['name'] = r[1]
#     #     user['age'] = r[2]
#     #     user['tel'] = r[3]
#     #     user['address'] = r[4]
#     #     users.append(user)
#     #
#     #     # print json.dumps(userlist, default=Users.to_json)
#     #     userlist_dic = Users.to_json(userlist)
#     #     print userlist_dic
#     #     # users = userlist.query.paginate(current_page, page_size, error_out=True)
#     #     # print users
#         rsp = make_response(userlist_json)
#         return rsp
#     else:
#         return 'w'

# 采用flask_restful实现接口
from flask_restful import Resource, Api, reqparse, fields, marshal_with, marshal
from flask import jsonify
from app.models import Users
from . import usermgr

api = Api(usermgr)

dataList_fields = {
           'account': fields.String,
           'open_id': fields.String,
           'password': fields.String,
           'data_role': fields.String,
           'data_access_level': fields.String,
           'create_time': fields.DateTime
       }


# 定义工具类
class Common:
    def return_true(self, data, current_page, page_size, total_results=10):
        succ = {
            "current_page": current_page,
            "dataList": data,
            "page_size": page_size,
            "total_results": total_results
        }
        return jsonify(succ)


common = Common()


# 定义userlist资源
class UserList(Resource):
    # @marshal_with(dataList_fields, envelope='dataList')
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('account', type=str)
        # action='append' 可以传入多个值
        parser.add_argument('role_ids', type=str, action='append')
        # required=True表示必选参数
        parser.add_argument('current_page', type=int, required=True)
        # required=True表示必选参数
        parser.add_argument('page_size', type=int, required=True)
        args = parser.parse_args()

        print args['account']
        print args['role_ids']
        print args['current_page']
        print args['page_size']

        if args['current_page']==1 or args['page_size']==20:
        # if args['account'] is '' or args['role_ids'] is '':
            dataList = Users.query.all()
            print common.return_true(marshal(dataList, dataList_fields), current_page=args['current_page'],
                                     page_size=args['page_size'], total_results=10)

            return common.return_true(marshal(dataList, dataList_fields), current_page=args['current_page'],
                                     page_size=args['page_size'], total_results=10)
        else:
            return 'w'


api.add_resource(UserList, '/authsys/api/usermgr/getuserlist')








