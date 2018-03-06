#!/usr/local/bin/venv/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/5 16:35
# @Author  : ShenFeng
# @Site    :
# @File    : cdt-auth.py.py
# @Software: PyCharm


import os
from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app.models import Users, Roles, Resources, RoleUser, RoleResource, Log, Menu, ResType


# 创建app实例
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# 初始化命令行
manager = Manager(app)
# 初始化数据库迁移
migrate = Migrate(app, db)


# 创建命令行上下文
def make_shell_context():
    return dict(app=app, db=db, Users=Users, Roles=Roles, Resources=Resources, RoleUser=RoleUser,
                RoleResource=RoleResource, Log=Log, Menu=Menu, ResType=ResType)


manager.add_command('shell', Shell(make_context=make_shell_context))
# 绑定数据库
manager.add_command('db', MigrateCommand)


# 运行项目
if __name__ == '__main__':
    manager.run()
