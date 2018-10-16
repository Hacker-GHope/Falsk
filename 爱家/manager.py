# -*- coding: utf-8 -*-
# @Time    : 2018/10/13 11:12
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : manager.py
# @Software: PyCharm

from flask import Flask
from flask_script import Manager

from app.models import db
from app.user_views import user_blueprint

app = Flask(__name__)

app.register_blueprint(blueprint=user_blueprint,url_prefix='/user')

app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/aj'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
