from email import message
from hmac import digest
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
    function = bottle.request.forms.get('function')
    k_coefficient = bottle.request.forms.get('k_coefficient')
    a_coefficient = bottle.request.forms.get('a_coefficient')
    b_coefficient = bottle.request.forms.get('b_coefficient')
    c_coefficient = bottle.request.forms.get('c_coefficient')
    x_value = bottle.request.forms.get('x_value')
    start_length = bottle.request.forms.get('start_length')
    end_length = bottle.request.forms.get('end_length')

    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    err_msg = "Ошибка: введите число!"

    if start_length == digest and start_length != "":
        sl = float(start_length)
    else:
        return template('plotting.tpl',message=err_msg, image_data="static\images\graph1.png", title='Построение графиков', year=datetime.now().year)
    
    if end_length == digest and end_length != "":
        el = float(end_length)
    else:
        return template('plotting.tpl',message=err_msg, image_data="static\images\graph1.png", title='Построение графиков', year=datetime.now().year)
    
    
    if function == 'linear':
        if k_coefficient == digest and k_coefficient != "":
            k = float(k_coefficient)
        else:
            return template('plotting.tpl', message=err_msg, image_data="static\images\graph1.png", title='Построение графиков', year=datetime.now().year)
        if b_coefficient == digest and b_coefficient != "":
            b = float(b_coefficient)
        else:
            return template('plotting.tpl', message=err_msg, image_data="static\images\graph1.png", title='Построение графиков', year=datetime.now().year)

        x = np.linspace(sl, el, 100)
        y = k * x + b
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Линейная функция: y = {}x + {}'.format(k, b))
        ax.grid(True)

    elif function == 'quadratic':
        if a_coefficient == digest and a_coefficient != "":
            a = float(a_coefficient)
        else:
            return template('plotting.tpl', message=err_msg, image_data="static\images\graph1.png", title='Построение графиков', year=datetime.now().year)
        if b_coefficient == digest and b_coefficient != "":
            b = float(b_coefficient)
        else:
            return template('plotting.tpl', message=err_msg, image_data="static\images\graph1.png", title='Построение графиков', year=datetime.now().year)
        if c_coefficient == digest and c_coefficient != "":
            c = float(c_coefficient)
        else:
            return template('plotting.tpl', message=err_msg, image_data="static\images\graph1.png", title='Построение графиков', year=datetime.now().year)

        x = np.linspace(sl, el, 100)
        y = a * x**2 + b * x + c
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Квадратичная функция: y = {}x^2 + {}x + {}'.format(a, b, c))
        ax.grid(True)

    elif function == 'power':
        if a_coefficient == digest and a_coefficient != "":
            a = float(a_coefficient)
        else:
            return template('plotting.tpl', message=err_msg, image_data="static\images\graph1.png", title='Построение графиков', year=datetime.now().year)

        x = np.linspace(sl, el, 100)
        y = x**a
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Степенная функция: y = x^{}'.format(a))
        ax.grid(True)

    canvas.draw()
    image = canvas.tostring_rgb().decode('latin-1')
    image_path = os.path.join("static/images", "graph1.png")
    canvas.print_png(image_path)

    return template('plotting.tpl', message="", image_data="static\images\graph1.png", title='Построение графиков', year=datetime.now().year)