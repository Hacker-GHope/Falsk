# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 9:49
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : manage.py
# @Software: PyCharm
import redis

from flask import Flask
from flask_script import Manager
from flask_session import Session

from user.views import user_blueprint
from user.models import db

app = Flask(__name__)
app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')

# 配置Session
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)

# 数据库的设置
# dialect + driver://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 获取Session对象，并初始化app
se = Session()
se.init_app(app)

# 绑定app和db
db.init_app(app)

manage = Manager(app=app)

if __name__ == '__main__':
    manage.run()
