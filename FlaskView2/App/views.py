# -*- coding: utf-8 -*
from flask import Blueprint, request, render_template, make_response, Response, abort, session

blue = Blueprint('blue', __name__)


def init_blue(app):
    app.register_blueprint(blue)


@blue.route('/')
def index():
    return "Index"


@blue.route('/sendrequest/', methods=["GET", "POST", "DELETE", "PUT", "PATCH"])
def send_request():
    print(request.args)

    print(type(request.args))

    print(request.form)

    print(type(request.form))

    print(request.headers)

    print(type(request.headers))

    return 'send success'


@blue.route('/getresponse/')
def get_response():
    # return 'Hello Sleeping'

    # result = render_template('Hello.html')
    #
    # print(result)
    #
    # print(type(result))
    #
    # return result

    # response = make_response("<h2>班主任说了两个月要去团建都没去</h2>")
    #
    # print(response)
    #
    # print(type(response))

    abort(401)

    response = Response("我自己造一个DIY")

    return response


@blue.errorhandler(401)
def handle_error(error):
    print(error)

    print(type(error))

    return 'What'


@blue.route('/login/', methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":

        username = request.form.get("username")

        response = Response("登录成功%s" % username)

        #response.set_cookie('username', username)
        session['username'] = username
        session['password'] = "110"

        return response


@blue.route('/mine/')
def mine():

    # username = request.cookie.get('username')

    username = session.get('username')

    print(session)

    print(type(session))

    return '欢迎回来:%s' % username
