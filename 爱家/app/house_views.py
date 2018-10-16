# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 20:11
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : house_views.py
# @Software: PyCharm

from flask import Blueprint, render_template, request

house_blueprint = Blueprint('house', __name__)


@house_blueprint.route('/my_house/', methods=['GET', 'POST'])
def my_house():
    if request.method == 'GET':
        return render_template('myhouse.html')
