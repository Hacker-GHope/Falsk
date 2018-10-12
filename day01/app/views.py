# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 13:58
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : views.py
# @Software: PyCharm

from flask import Blueprint, redirect, url_for, request, \
    make_response, render_template, abort,session


from utils.functions import is_login

# 获取蓝图对象，指定蓝图别名
blue = Blueprint('app', __name__)


@blue.route('/')
def hello_world():
    return 'Hello Word!'


# 路由匹配规则
# 1、<id>: 默认接收的类型是str
# 2、<string:id>: 指定接收的类型是str（字符串）
# 3、<int:id>: 指定接收的类型是int（整形）
# 4、<float:uid>: 指定接收的类型是float（浮点型）
# 4、<path:upath>: 指定接收的类型是path(URl中的路径)
@blue.route('/get_id/<id>/')
def get_id(id):
    # 匹配str类型的id值
    return 'id: %s' % id


@blue.route('/get_int_id/<int:id>/')
def get_int_id(id):
    # 匹配int类型的id值
    return 'id: %d' % id


@blue.route('/get_float_id/<float:uid>/')
def get_float_id(uid):
    # 匹配float类型的uid值
    return 'id: %.3f' % uid


@blue.route('/get_path/<path:upath>/')
def get_path(upath):
    # 匹配path类型的upath值
    return 'path: %s' % upath


@blue.route('/redirect/')
def redirect_hello():
    # 实现跳转
    # 1、硬编码
    # return redirect('/app/')
    # 2、反向解析redirect(url_for('蓝图别名.跳转的函数名'))
    # return redirect(url_for('app.hello_world'))
    return redirect(url_for('app.get_id', id=3))


@blue.route('/request/', methods=['GET', 'POST', 'PUT'])
def get_request():
    # 请求上下文 request
    # 获取GET请求传递的参数：request.args.get(key)/request.args.getlist(key)
    # 获取POST、PUT、PATCH、DELETE请求传递的参数：request.form.get(key)/request.form.getlist(key)
    # 判断HTTP的请求方式：request.method
    pass


@blue.route('/response/', methods=['GET'])
@is_login
def get_response():
    # 创建响应
    # res = make_response('人生苦短，我用Python！',200)
    # 绑定cookie，set_cookie(key,value,max_age,expires)
    # 删除cookie，set_cookie(key )
    res_index = render_template('index.html')
    res = make_response(res_index, 200)
    return res


@blue.route('/index/', methods=['GET'])
def index():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    try:
        a / b
    except Exception as e:
        print(e)
        # 抛出错误
        abort(500)

    return render_template('index.html')


@blue.errorhandler(500)
def error500(exception):
    return '捕捉异常，错误信息为: %s' % exception


@blue.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        # 获取页面传递参数
        username = request.form.get('username')
        password = request.form.get('password')
        # 验证用户名和密码是否正确
        if username == '111' and password == '222':
            # 验证通过，向session中存入登录成功的标识符
            session['login_status'] = 1
            return redirect(url_for('app.get_response'))
        else:
            return render_template('login.html')
