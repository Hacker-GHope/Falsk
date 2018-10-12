# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 10:03
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : views.py
# @Software: PyCharm
import os

from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from user.forms import UserRegisterForm
from user.modles import db, User
from utils.setting import UPLOAD_DIR

user_blueprint = Blueprint('user', __name__)
login_manager = LoginManager()


@user_blueprint.route('/create_db/')
def create_db():
    db.create_all()
    return '创建成功'


@user_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    form = UserRegisterForm()
    if request.method == 'GET':
        return render_template('register.html', form=form)

    if request.method == 'POST':
        # 验证提交的字段信息
        if form.validate():
            username = form.username.data
            password = form.password.data
            # 实现注册，保存用户信息到User模型中
            user = User()
            user.username = username
            user.password = generate_password_hash(password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.login'))
        else:
            # 验证失败，from.errors中存在错误信息
            return render_template('register.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


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
        if user:
            # 获取到用户，进行密码判断
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('user.index'))
            else:
                error = '密码错误'
                return render_template('login.html', error=error)
        else:
            error = '该用户尚未注册，请先行注册后在进行登录！'
            return render_template('login.html', error=error)


@user_blueprint.route('/index/',methods=['GET','POST'])
@login_required
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        # 获取
        icons = request.files.get('icons')
        # 保存
        file_path = os.path.join(UPLOAD_DIR,icons.filename)
        icons.save(file_path)
        user = current_user
        user.icons = os.path.join('upload',icons.filename)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.index'))


@user_blueprint.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))
