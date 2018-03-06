#!/usr/local/bin/venv/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/5 16:35
# @Author  : ShenFeng
# @Site    :
# @File    : cdt-auth.py.py
# @Software: PyCharm


from app import create_app, db
from app.models import Users, Roles, Resources, RoleUser, RoleResource, Log, Menu, ResType
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


# 创建app实例
app = create_app('default')
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


# 创建超级管理员角色
@manager.command
def create_role_superadmin():
    superadmin = Roles(role_id=0, role_name='Superadmin', b_inside=1, b_super=1)
    db.session.add(superadmin)
    db.session.commit()


# 创建默认Guest角色
@manager.command
def create_role_guest():
    guest = Roles(role_id=10000, role_name='Guest', b_inside=1, data_scope=2)
    db.session.add(guest)
    db.session.commit()


# 创建超级管理员账户superadmin
@manager.command
def create_superadmin():
    superadmin = Users(open_id='11111', account='superadmin', passwd='shenfeng', b_inside=1)
    db.session.add(superadmin)
    db.session.commit()


# 创建默认用户guest
@manager.command
def create_guest():
    guest = Users(open_id='22222', account='guest', passwd='shenfeng', b_inside=1)
    db.session.add(guest)
    db.session.commit()


# 运行项目
if __name__ == '__main__':
    manager.run()