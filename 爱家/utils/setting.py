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
