# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 9:57
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : views.py
# @Software: PyCharm

from flask import Blueprint, render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from utils.functions import is_login
from user.models import db, User

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not all([username, password]):
            return render_template('login.html')

        user = User.query.filter(User.username == username).first()

        if user and check_password_hash(user.password,password):
            session['login_status'] = 1
            return redirect(url_for('user.index'))
        else:
            return render_template('login.html')


@user_blueprint.route('/index/', methods=['GET'])
@is_login
def index():
    if request.method == 'GET':
        return render_template('index.html')


@user_blueprint.route('/scores/', methods=['GET'])
def scores():
    stu_scores = [80, 56, 31, 89, 76, 34]
    content_h2 = '<h2>hello python</h2>'
    return render_template('scores.html', stu_scores=stu_scores, content_h2=content_h2)


@user_blueprint.route('/create_db/')
def create_db():
    db.create_all()
    return '创建表成功'


@user_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not all([username, password]):
            return render_template('register.html')
        # 保存注册信息
        user = User()
        user.username = username

        user.password = generate_password_hash(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.login'))
