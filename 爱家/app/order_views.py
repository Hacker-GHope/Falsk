# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 19:48
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : order_views.py
# @Software: PyCharm

from flask import Blueprint, request, render_template

order_blueprint = Blueprint('order', __name__)


@order_blueprint.route('/order/', methods=['GET'])
def order():
    if request.method == 'GET':
        return render_template('order.html')


@order_blueprint.route('/orders/', methods=['GET'])
def orders():
    if request.method == 'GET':
        return render_template('orders.html')
