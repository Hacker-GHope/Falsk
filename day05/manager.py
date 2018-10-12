# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 9:58
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : manager.py
# @Software: PyCharm


from flask import Flask
from flask_script import Manager

from user.modles import db
from user.views import user_blueprint, login_manager

app = Flask(__name__)

app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')

app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/f_login'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 未登录状态跳转地址
login_manager.login_view = 'user.login'


db.init_app(app)

login_manager.init_app(app)

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
