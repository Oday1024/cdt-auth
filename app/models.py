#!/usr/local/bin/venv/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/5 16:36
# @Author  : ShenFeng
# @Site    : 
# @File    : models.py
# @Software: PyCharm


from datetime import datetime
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app, request
from . import db


class User(db.Model):
    __tablename__ = 'td_user'
    __table_args__ = {
        'schema': 'sys'
    }
    id = db.Column(db.Integer, primary_key=True)
    open_id = db.Column(db.String(32), unique=True)
    account = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    deleted = db.Column(db.Integer)
