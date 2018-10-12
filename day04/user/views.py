# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 9:30
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : views.py
# @Software: PyCharm

from flask import Blueprint, request, render_template
from sqlalchemy import or_, not_

from user.models import db, Students, Class, Course

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
    names = ['贪狼', '释天', '无相', '青冥', '太上', '无为', '北斗', '七殇', '三才', '布衣']
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


@blue.route('/create_cla_many/')
def create_cla_many():
    # 实现创建多个功能
    names = ['天干', '地支', '星宿', '百鬼', '三千']
    cla_list = []
    for name in names:
        cla = Class()
        cla.c_name = name
        # 避免多次IO操作
        # stu.save()
        cla_list.append(cla)
    db.session.add_all(cla_list)
    db.session.commit()
    return '创建多个班级信息成功'


@blue.route('/create_course/')
def create_course():
    names = ['Linux', 'C', 'Java', 'Android', 'C++', 'C#', 'Shell', 'Python']
    course_list = []
    for name in names:
        course = Course()
        course.c_name = name
        course_list.append(course)
    db.session.add_all(course_list)
    db.session.commit()
    return '添加班级信息'


@blue.route('/add_stu_cou/')
def add_stu_cou():
    stu = Students.query.get(8)
    # 学生对象查找课程信息,stu.cou
    cou1 = Course.query.get(1)
    cou2 = Course.query.get(2)
    cou3 = Course.query.get(3)
    # 绑定学生和课程的关联关系
    stu.cou.append(cou1)
    stu.cou.append(cou2)
    stu.cou.append(cou3)
    stu.save()
    return '南山选课成功'


@blue.route('rel_stu_cla')
def rel_stu_cla():
    stus_ids = [1, 3, 4]
    for id in stus_ids:
        stu = Students.query.get(id)
        # 在flask中stu.s_c获取的值为int型
        # 在fDjango中stu.s_c获取的是对象，stu_c_id获取到int类型
        stu.s_g = 1
        stu.save()
    return '关联学生和班级'


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
    stus = Students.query.filter(Students.id.in_([2, 3, 4, 5]))

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
    stus = Students.query.filter(Students.s_name.contains('王'), Students.s_age == 18)

    # 查询姓名中包含一的，或年龄等于18的
    stus = Students.query.filter(or_(Students.s_name.contains('王'), Students.s_age == 18))
    # 查询姓名中包不含一的，且年龄等于18的
    stus = Students.query.filter(not_(Students.s_name.contains('王')), Students.s_age == 18)

    return '查询学生'


@blue.route('/sel_stu_by_cla/')
def sel_stu_by_cla():
    cla = Class.query.filter(Class.c_name == '天干').first()
    stus = cla.students
    return '通过班级查找学生信息'


@blue.route('/sel_cla_by_stu/')
def sel_cla_by_stu():
    stu = Students.query.get(5)
    # 获取班级，学生对象.backref
    cla = stu.cla
    return '通过学生查找班级信息'


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


# 实现分页
@blue.route('/paginate/')
def stu_page():
    page = int(request.args.get('page', '1'))
    # 1.offset+limit
    stus = Students.query.offset((page - 1) * 2).limit(2)
    # 2.切片
    stus = Students.query.all()[(page - 1) * 2:page * 2]
    # 3.sql
    sql = 'select * from students limit %s,%s' % ((page - 1) * 2, 2)
    stus = db.session.execute(sql)
    # paginate()方法
    paginate = Students.query.paginate(page, 3)
    stus = paginate.items
    return render_template('stus.html', stus=stus, paginate=paginate)
