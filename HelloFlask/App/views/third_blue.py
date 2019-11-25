from flask import Blueprint

third = Blueprint('third',__name__)

@third.route('/hi/')
def hi():
    return 'hei third'