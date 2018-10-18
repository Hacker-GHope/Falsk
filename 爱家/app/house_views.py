# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 20:11
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : house_views.py
# @Software: PyCharm
import os

from flask import Blueprint, render_template, request, session, jsonify

from app.models import User, House, Facility, Area, HouseImage
from utils import status_code
from utils.config import Config

house_blueprint = Blueprint('house', __name__)


@house_blueprint.route('/my_house/', methods=['GET', 'POST'])
def my_house():
    if request.method == 'GET':
        return render_template('myhouse.html')


@house_blueprint.route('/my_auth/')
def my_auth():
    """
    验证当前用户是否完成实名认证
    """
    user_id = session['user_id']
    user = User.query.get(user_id)
    if user.id_name:
        # 已经完成实名认证，查询当前用户的房屋信息
        house_list = House.query.filter(House.user_id == user_id).order_by(House.id.desc())
        house_list2 = []
        for house in house_list:
            house_list2.append(house.to_dict())
        return jsonify(code='200', hlist=house_list2)
    else:
        # 没有完成实名认证
        return jsonify(status_code.MYHOUSE_USER_IS_NOT_AUTH)


@house_blueprint.route('/area_facility/')
def area_facility():
    # 查询地址
    area_list = Area.query.all()
    area_dict_list = [area.to_dict() for area in area_list]
    # 查询设施
    facility_list = Facility.query.all()
    facility_dict_list = [facility.to_dict() for facility in facility_list]
    # 构造结果并返回
    return jsonify(area=area_dict_list, facility=facility_dict_list)


@house_blueprint.route('/new_house/', methods=['GET', 'POST'])
def new_house():
    if request.method == 'GET':
        return render_template('newhouse.html')

    if request.method == 'POST':
        # 接收用户信息
        params = request.form.to_dict()
        facility_ids = request.form.getlist('facility')

        # 创建用户信息
        house = House()
        house.user_id = session['user_id']
        house.area_id = params.get('area_id')
        house.title = params.get('title')
        house.price = params.get('price')
        house.address = params.get('address')
        house.room_count = params.get('room_count')
        house.acreage = params.get('acreage')
        house.beds = params.get('beds')
        house.unit = params.get('unit')
        house.capacity = params.get('capacity')
        house.deposit = params.get('deposit')
        house.min_days = params.get('min_days')
        house.max_days = params.get('max_days')
        # 根据设施的编号查询设施对象
        if facility_ids:
            facility_list = Facility.query.filter(Facility.id.in_(facility_ids)).all()
            house.facilities = facility_list
        house.add_update()
        # 返回结果
        return jsonify(code='200', house_id=house.id)


@house_blueprint.route('/image_house/', methods=['POST'])
def image_house():
    if request.method == 'POST':
        # 接收房屋编号
        house_id = request.form.get('house_id')
        # 接收图片信息
        f1 = request.files.get('house_image')
        # 保存到图片
        con = Config()
        url = os.path.join(os.path.join(con.UPLOAD_FOLDER, 'house'), f1.filename)
        f1.save(url)

        # 保存图片对象
        image = HouseImage()
        image.house_id = house_id
        image.url = os.path.join('/static/upload/house', f1.filename)
        image.add_update()
        # 房屋的默认图片
        house = House.query.get(house_id)
        if not house.index_image_url:
            house.index_image_url = os.path.join('/static/upload/house', f1.filename)
            house.add_update()
        # 返回图片信息
        return jsonify(code='200', url=os.path.join('/static/upload/house', f1.filename))


@house_blueprint.route('/detail/')
def detail():
    return render_template('detail.html')


@house_blueprint.route('/detail/<int:id>/')
def house_detail(id):
    # 查询房屋信息
    house = House.query.get(id)
    # 查询设施信息
    facility_list = house.facilities
    facility_dict_list = [facility.to_dict() for facility in facility_list]
    # 判断当前房屋信息是否为当前登录的用户发布，如果是则不显示预订按钮
    booking = 1
    if 'user_id' in session:
        if house.user_id == session['user_id']:
            booking = 0

    return jsonify(house=house.to_full_dict(), facility_list=facility_dict_list, booking=booking)
