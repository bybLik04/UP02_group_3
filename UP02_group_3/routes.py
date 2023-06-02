"""
Routes and views for the bottle application.
"""

from email import message
from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    return dict(
        title='Главная',
        year=datetime.now().year
    )

@route('/authors')
@view('authors')
def authors():
    return dict(
        title='Об авторах',
        year=datetime.now().year
    )

@route('/approx2')
@view('approxim_2deg')
def authors():
    return dict(
        image_data='static\images\graph_strt.png',
        title='Аппроксимация 2-й ст',
        year=datetime.now().year
    )

@route('/plott')
@view('plotting')
def authors():
    return dict(
        title='Построение графиков',
        message='',
        image_data="static\images\graph0.png",
        year=datetime.now().year
    )

@route('/approx1')
@view('approxim_1deg')
def authors():
    return dict(
        title='Аппроксимация 1-й ст',
        k = 0,
        b = 0,
        r = 0,
        ex = '',
        image_data='static\images\graph_strt.png',
        year=datetime.now().year
    )