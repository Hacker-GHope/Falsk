# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 9:57
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : models.py
# @Software: PyCharm

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    # 如果不写tablename参数，数据库中的表明为user(类名的小写)
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(10),unique=True,nullable=False)
    password = db.Column(db.String(128),nullable=False)









