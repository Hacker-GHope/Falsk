# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 10:09
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : forms.py
# @Software: PyCharm

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError

from user.modles import User


class UserRegisterForm(FlaskForm):
    # 定义密码和账号都是必填项
    username = StringField('账号', validators=[DataRequired()])
    password = StringField('密码', validators=[DataRequired()])
    password2 = StringField('确认密码',
                            validators=[DataRequired(), EqualTo('password', '密码不一致')])

    submit = SubmitField('注册')

    def validate_username(self, field):
        user = User.query.filter(User.username == field.data).first()
        if user:
            raise ValidationError('该用户已存在')
        if len(field.data) < 3:
            raise ValidationError('注册用户名不能少于3个字符')


class UserLoginForm(FlaskForm):
    # 定义密码和账号都是必填项
    username = StringField('账号', validators=[DataRequired()])
    password = StringField('密码', validators=[DataRequired()])
    password2 = StringField('确认密码',
                            validators=[DataRequired(), EqualTo('password', '密码不一致')])

    submit = SubmitField('登录')

    def validate_username(self, field):
        user = User.query.filter(User.username == field.data).first()
        if not user:
            raise ValidationError('该用户不存在')

