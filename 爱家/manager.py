# -*- coding: utf-8 -*-
# @Time    : 2018/10/13 11:12
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : manager.py
# @Software: PyCharm


from flask_script import Manager

from utils.app import create_app

# 创建app
app = create_app()

# 使用Manger管理app
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
