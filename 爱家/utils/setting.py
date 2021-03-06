# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 11:19
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : setting.py
# @Software: PyCharm

import os

# 项目路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 静态文件
static_dir = os.path.join(BASE_DIR, 'static')

# 模板文件
template_dir = os.path.join(BASE_DIR, 'templates')

# 数据库配置
MYSQL_DATABASES = {
    'DRIVER': 'mysql',
    'DH': 'pymysql',
    'ROOT': 'root',
    'PASSWORD': 'root',
    'HOST': '127.0.0.1',
    'PORT': '3306',
    'NAME': 'aj'
}

# 会话缓存配置
REDIS_DATABASES = {
    'HOST': '127.0.0.1',
    'PORT': '6379'
}
