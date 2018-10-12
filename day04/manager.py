# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 9:24
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : manager.py
# @Software: PyCharm

from flask import Flask
from flask_script import Manager
from flask_debugtoolbar import DebugToolbarExtension

from user.models import db
from user.views import blue

app = Flask(__name__)

app.register_blueprint(blueprint=blue, url_prefix='/user')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key'

# 开启debug模式
app.debug = True

# 初始化app和db
db.init_app(app)

toolbar = DebugToolbarExtension()
toolbar.init_app(app)

manager = Manager(app=app)

if __name__ == '__main__':
    manager.run()
