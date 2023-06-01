"""
Routes and views for the bottle application.
"""

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
        message='Об авторах',
        year=datetime.now().year
    )

@route('/approx2')
@view('approxim_2deg')
def authors():
    return dict(
        title='Аппроксимация 2-й ст',
        message='Аппроксимация 2-й ст',
        year=datetime.now().year
    )

@route('/plott')
@view('plotting')
def authors():
    return dict(
        title='Построение графиков',
        message='Построение графиков',
        image_data="static\images\var1.jpg",
        year=datetime.now().year
    )

@route('/approx1')
@view('approxim_1deg')
def authors():
    return dict(
        title='Аппроксимация 1-й ст',
        message='Аппроксимация 1-й ст',
        year=datetime.now().year
    )