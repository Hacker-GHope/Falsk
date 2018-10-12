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
    s_c = db.Column(db.Integer, db.ForeignKey('cla.id'), nullable=True)

    def save(self):
        db.session.add(self)
        db.session.commit()


class Class(db.Model):
    __tablename__ = 'cla'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_name = db.Column(db.String(30), unique=True, nullable=False)
    students = db.relationship('Students', backref='cla')


s_c = db.Table('s_c',
               db.Column('s_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
               db.Column('c_id', db.Integer, db.ForeignKey('course.id'), primary_key=True))


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_name = db.Column(db.String(30), unique=True, nullable=False)
    students = db.relationship('Students', secondary=s_c, backref='cou')
