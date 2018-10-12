# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 9:31
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : models.py
# @Software: PyCharm

from flask_sqlalchemy import SQLAlchemy

# 获取对象
db = SQLAlchemy()


class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(10), unique=False, nullable=False)
    s_age = db.Column(db.Integer, default=18)

    def save(self):
        db.session.add(self)
        db.session.commit()
