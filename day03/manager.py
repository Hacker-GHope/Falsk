# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 9:24
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : manager.py
# @Software: PyCharm

from flask import Flask
from flask_script import Manager

from user.models import db
from user.views import blue

app = Flask(__name__)

app.register_blueprint(blueprint=blue, url_prefix='/user')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化app和db
db.init_app(app)

manager = Manager(app=app)

if __name__ == '__main__':
    manager.run()
