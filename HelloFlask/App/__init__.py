#coding=utf-8
from flask import Flask

# from App.views.second_blue import second
from flask_sqlalchemy import  SQLAlchemy

from App.ext import init_ext
from App.views import init_view


def create_app():
    app = Flask(__name__)

    # app.register_blueprint(blue)
    #
    # app.register_blueprint(second)

    #uri   数据库+驱动：//用户名：密码@主机：端口/具体哪一个库
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqlite.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_ext(app)

    init_view(app=app)

    return app