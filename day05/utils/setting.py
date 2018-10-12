# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 16:37
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : setting.py
# @Software: PyCharm

import os

# 基础路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# STATIC路径
STATIC_DIR = os.path.join(BASE_DIR,'static')

# TEMPLATES路径
TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')

# 上传路径
UPLOAD_DIR = os.path.join(os.path.join(STATIC_DIR,'media'),'upload')