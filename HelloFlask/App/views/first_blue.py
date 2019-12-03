# coding=utf-8
from flask import Blueprint, render_template

from App.models import models, User

blue = Blueprint('blue', __name__)


@blue.route('/')
def index():
    # return '我是蓝图的主页'
    return render_template('index.html', msg="It is a messge from index.html")

@blue.route('/dropdb/')
def dropdb():
    models.drop_all()

    return '删除成功'

@blue.route('/createdb/')
def createdb():
    models.create_all()

    return '创建成功'

@blue.route('/adduser/')
def add_user():
    user = User()
    user.username = "Tom"

    user.save()
    # models.session.add(user)
    # models.session.commit()

    return '增加创建成功'