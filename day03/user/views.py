# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 9:30
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : views.py
# @Software: PyCharm

from flask import Blueprint
from sqlalchemy import or_, not_

from user.models import db, Students

blue = Blueprint('user', __name__)


@blue.route('/')
def hello():
    return 'hello'


@blue.route('/create_db/')
def create_db():
    # 用于初次创建模型
    db.create_all()
    return '创建成功'


@blue.route('/drop_db/')
def drop_db():
    # 删除数据库中的所有的表
    db.drop_all()
    return '删除成功'


@blue.route('/create_stu/')
def create_stu():
    # 实现创建功能
    stu = Students()
    stu.s_name = '小明1'
    stu.save()
    return '创建学生信息成功'


@blue.route('/create_stu_many/')
def create_stu_many():
    # 实现创建多个功能
    names = ['纳兰', '性德', '容若', '太白', '牧之', '青莲', '武斗', '南山', '一笑', '殺']
    stu_list = []
    for name in names:
        stu = Students()
        stu.s_name = name
        # 避免多次IO操作
        # stu.save()
        stu_list.append(stu)
    db.session.add_all(stu_list)
    db.session.commit()
    return '创建多个学生信息成功'


@blue.route('/sel_stu/')
def sel_stu():
    # 查询，filter(),filter_by()
    # 返回类型是querybase
    stu = Students.query.filter(Students.s_name == '纳兰')
    stu = Students.query.filter_by(s_name='纳兰')
    # all(),first()
    stus = Students.query.all()
    stu = Students.query.filter(Students.s_age == 19).first()
    # 执行SQL
    sql = 'select * from students;'
    stus = db.session.execute(sql)

    # 模糊查询
    # 姓名中包含一的学生信息
    # select * from students where s_name like '%一%'
    stu = Students.query.filter(Students.s_name.contains('一'))
    # 以一开始
    # select * from students where s_name like '一%'
    stu = Students.query.filter(Students.s_name.startswith('一'))

    # 查询id在某个范围之内的学生信息
    # select * from student where id in (1,2,3,4,5)
    stus = Students.query.filter(Students.id.in_([2,3,4,5]))

    # 查询年龄大于18的学生信息
    stus = Students.query.filter(Students.s_age > 18)
    stus = Students.query.filter(Students.s_age.__gt__(18))

    # 查询id为3的学生信息
    # get()获取主键对应的行数据
    stu = Students.query.filter(Students.id == 2).first()
    stu = Students.query.get(3)

    # offset + limit
    stus = Students.query.limit(3)
    stus = Students.query.offset(0).limit(3)

    # order_by()
    stus = Students.query.order_by('id')
    # stus = Students.query.order_by('-id')

    # 查询姓名中包含一的，且年龄等于18的
    stus = Students.query.filter(Students.s_name.contains('王'),Students.s_age == 18)

    # 查询姓名中包含一的，或年龄等于18的
    stus = Students.query.filter(or_(Students.s_name.contains('王'), Students.s_age == 18))
    # 查询姓名中包不含一的，且年龄等于18的
    stus = Students.query.filter(not_(Students.s_name.contains('王')), Students.s_age == 18)

    return '查询学生'


@blue.route('/delete_stu/<int:id>/')
def delete_stu(id):
    stu = Students.query.filter(Students.id == id).first()
    db.session.delete(stu)
    db.session.commit()
    return '删除成功'


@blue.route('/update_stu/<int:id>/')
def update_stu(id):
    stu = Students.query.filter_by(id=id).first()
    stu.s_name = 'GHope'
    stu.save()
    return '修改成功'
