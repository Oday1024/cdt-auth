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


class Users(db.Model):
