#coding=utf-8
from .first_blue import blue
from .second_blue import second
from .third_blue import third

"""
def init_route(app):

    @app.route('/')
    def hello_world():
        return 'Hello world!'

    @app.route('/hello/')
    def hello():
        return 'asd hello what'

    @app.route('/hi/')
    def hi():
        return 'hi what?'
"""
def init_view(app):
    app.register_blueprint(blue)
    app.register_blueprint(second)
    app.register_blueprint(third)
