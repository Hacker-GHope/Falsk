# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 9:50
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : status_code.py
# @Software: PyCharm

OK = 200
SUCCESS = {'code': 200, 'msg': '请求成功'}
DATABASE_ERROR = {'code': 500, 'msg': '内部错误'}

# 用户模块
USER_NOT_ALL = {'code': 10000, 'msg': '参数不完整'}
USER_MOBILE_ERROR = {'code': 10001, 'msg': '非法手机号'}
USER_IMAGECODE_ERROR = {'code': 10002, 'msg': '验证码错误'}
USER_PASSWORD_ERROR = {'code': 10003, 'msg': '密码不一致'}
USER_ERROR = {'code': 1004, 'msg': '用户已存在'}
