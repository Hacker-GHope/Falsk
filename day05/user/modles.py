# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 10:03
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : modles.py
# @Software: PyCharm

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(128),  nullable=False)
    icons = db.Column(db.String(100),nullable=True)
