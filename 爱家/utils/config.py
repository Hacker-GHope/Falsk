# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 11:09
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : config.py
# @Software: PyCharm
import os

from utils.setting import BASE_DIR


class Config():
    # 上传图片地址
    UPLOAD_FOLDER = os.path.join(os.path.join(BASE_DIR, 'static'), 'media')
