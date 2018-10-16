# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 11:32
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : user_views.py
# @Software: PyCharm
import random
import re

from flask import Blueprint, render_template, redirect, url_for, request, session, jsonify

from app.models import db, User
from utils import status_code

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/create_db/', methods=['GET'])
def create_db():
    db.create_all()
    return '创建成功'


@user_blueprint.route('/get_code/', methods=['GET'])
def get_code():
    code = ''
    s = '1234567890qwertyuiopasdfghjklzxcvbnm'
    for i in range(4):
        code += random.choice(s)
    session['code'] = code
    return jsonify(code=200, msg='请求成功', data=code)


@user_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        mobile = request.form.get('mobile')
        imageCode = request.form.get('imageCode')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        # 效验参数完整
        if not all([mobile, imageCode, password, password2]):
            return jsonify(status_code.USER_NOT_ALL)
        # 效验手机号是否合法
        if not re.match(r'^1[3456789]\d{9}$', mobile):
            return jsonify(status_code.USER_MOBILE_ERROR)
        # 效验验证码是否正确
        if session.get('code') != imageCode:
            return jsonify(status_code.USER_IMAGECODE_ERROR)
        # 效验密码一致性
        if password != password2:
            return jsonify(status_code.USER_PASSWORD_ERROR)
        # 效验用户是否已存在
        if User.query.filter(User.phone == mobile).count():
            return jsonify(status_code.USER_ERROR)
        # 创建用户信息
        user = User()
        user.phone = mobile
        user.password = password
        user.name = mobile
        try:
            user.add_update()
            return jsonify(status_code.SUCCESS)
        except:
            return jsonify(status_code.DATABASE_ERROR)


@user_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        mobile = request.form.get('mobile')
        password = request.form.get('password')
        # 效验信息完整
        if not all([password, mobile]):
            return jsonify(status_code.USER_NOT_ALL)
        # 效验手机号是否合法
        if not re.match(r'^1[3456789]\d{9}$', mobile):
            return jsonify(status_code.USER_MOBILE_ERROR)
        user = User.query.filter(User.phone == mobile).first()
        # 效验用户是否存在
        if user:
            if user.check_pwd(password):
                # 效验密码是否正确
                session['user_id'] = user.id
                return jsonify(status_code.SUCCESS)
            else:
                return jsonify(status_code.USER_PASSWORD_ERROR)
        else:
            return jsonify(status_code.USER_ERROR)


@user_blueprint.route('/my/', methods=['GET', 'POST'])
def my():
    if request.method == 'GET':
        return render_template('my.html')
