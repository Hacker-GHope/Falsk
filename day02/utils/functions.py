# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 10:59
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : functions.py
# @Software: PyCharm
from functools import wraps

from flask import redirect, url_for, session


def is_login(func):
    @wraps(func)
    def check_status(*args, **kwargs):
        try:
            session['login_status']
        except:
            return redirect(url_for('user.login'))
        return func(*args, **kwargs)

    return check_status
