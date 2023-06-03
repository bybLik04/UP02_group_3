import bottle
import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from bottle import template, post
from datetime import datetime
import os

matplotlib.use('Agg')

@post('/plott', method='POST')
def handle_plot_request():
    # получаем коэффициенты с полей ввода и заносим в переменные
    function = bottle.request.forms.get('function')
    k_coefficient = bottle.request.forms.get('k_coefficient')
    a_coefficient = bottle.request.forms.get('a_coefficient')
    b_coefficient = bottle.request.forms.get('b_coefficient')
    c_coefficient = bottle.request.forms.get('c_coefficient')
    x_value = bottle.request.forms.get('x_value')
    start_length = bottle.request.forms.get('start_length')
    end_length = bottle.request.forms.get('end_length')

    fig = Figure() # создание новой фигуры
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111) # новая область рисования
    err_msg = "Ошибка: введите число!"

    if start_length.isdigit() and start_length != "": # проверка на пустоту и числа
        sl = float(start_length)
    else:
        return template('plotting.tpl',message=err_msg, image_data="static\images\graph0.png", title='Построение графиков', year=datetime.now().year)
    
    if end_length.isdigit() and end_length != "":
        el = float(end_length)
    else:
        return template('plotting.tpl',message=err_msg, image_data="static\images\graph0.png", title='Построение графиков', year=datetime.now().year)
    
    
    if function == 'linear': # при нажатии кнопки решить выбрана линейная функция
        if k_coefficient.isdigit() and k_coefficient != "":
            k = float(k_coefficient)
        else:
            return template('plotting.tpl', message=err_msg, image_data="static\images\graph0.png", title='Построение графиков', year=datetime.now().year)

        if b_coefficient.isdigit() and b_coefficient != "":
            b = float(b_coefficient)
        else:
            return template('plotting.tpl', message=err_msg, image_data="static\images\graph0.png", title='Построение графиков', year=datetime.now().year)

        x = np.linspace(sl, el, 100)
        y = k * x + b
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Линейная функция: y = {}x + {}'.format(k, b))
        ax.grid(True) # сетка на графике

    elif function == 'quadratic': # при нажатии кнопки решить выбрана квадратичная функция
        if a_coefficient.isdigit() and a_coefficient != "":
            a = float(a_coefficient)
        else:
            return template('plotting.tpl', message=err_msg, image_data="static\images\graph0.png", title='Построение графиков', year=datetime.now().year)

        if b_coefficient.isdigit() and b_coefficient != "":
            b = float(b_coefficient)
        else:
            return template('plotting.tpl', message=err_msg, image_data="static\images\graph0.png", title='Построение графиков', year=datetime.now().year)

        if c_coefficient.isdigit() and c_coefficient != "":
            c = float(c_coefficient)
        else:
            return template('plotting.tpl', message=err_msg, image_data="static\images\graph0.png", title='Построение графиков', year=datetime.now().year)

        x = np.linspace(sl, el, 100)
        y = a * x**2 + b * x + c
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Квадратичная функция: y = {}x^2 + {}x + {}'.format(a, b, c))
        ax.grid(True)

    elif function == 'power': # при нажатии кнопки решить выбрана степенная функция
        if a_coefficient.isdigit() and a_coefficient != "":
            a = float(a_coefficient)
        else:
            return template('plotting.tpl', message=err_msg, image_data="static\images\graph0.png", title='Построение графиков', year=datetime.now().year)

        x = np.linspace(sl, el, 100)
        y = x**a
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Степенная функция: y = x^{}'.format(a))
        ax.grid(True)

    canvas.draw() # строим график
    image_path = os.path.join("static/images", "graph1.png") # путь
    canvas.print_png(image_path) # сохранение картинки

    # если нет ошибок
    return template('plotting.tpl', message="", image_data="static\images\graph1.png", title='Построение графиков', year=datetime.now().year)