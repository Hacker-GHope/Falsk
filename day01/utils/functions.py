# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 17:31
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : functions.py
# @Software: PyCharm
from functools import wraps

from flask import redirect,session,url_for


def is_login(func):
    @wraps(func)
    def check(*args,**kwargs):
        try:
            session['login_status']
        except:
            return redirect(url_for('app.login'))
        return func(*args,**kwargs)

    return check
