import random
from bottle import route, run, request, template, post
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

@post('/approx2', method='POST')
def approx2():
    if request.forms.get('dg2_btn'):
        try:
            err_msg='Ошибка входных данных!'

            # Получение коэффициентов из формы
            x = np.array(request.forms.get('X').split(), dtype=float)
            y = np.array(request.forms.get('Y').split(), dtype=float)

            #проверка на то, чтобы график не был одной точкой
            trigg = False
            for i in range(1, len(x)):
                if x[i] != x[0]:
                    trigg = True
                else:
                    trigg = False
            for i in range(1, len(y)):
                if y[i] != y[0]:
                    trigg = True
                else:
                    trigg = False

            # Основные вычисления
            A = np.vstack([x**2, x, np.ones(len(x))]).T #создание матрицы
            k, b, c = np.linalg.lstsq(A, y, rcond=None)[0] #получение коэффициентов квадратичной линии регрессии
            y_pred = k*x**2 + b*x + c #аппроксимация данных методом наименьших квадратов
            r2 = r2_score(y, y_pred)  #вычисление коэффициента детерминации

            # построение графика
            fig, ax = plt.subplots(figsize=(5, 5))
            ax.plot(x, y, 'o', label='Исходные данные', markersize=5)
            ax.plot(x, k * x**2 + b * x, 'r', label='Приближенная линия')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.legend()
            ax.grid(True)

            plt.savefig('static/images/square1.png', dpi=300, bbox_inches='tight') #сохранение построенного графика
            msg='Коэффициенты квадратичной линии регрессии: a0={}, a1={} a2={} \nКоэффициент детерминированности R2={}'.format(k.round(), b.round(), c.round(), r2.round())

            # Возвращает темплейт
            if trigg != True:
                return template('approxim_2deg.tpl', title='Аппроксимация 2-й ст.', image_data='static\images\graph_strt.png', message=err_msg)
            else:
                return template('approxim_2deg.tpl', title='Аппроксимация 2-й ст.', image_data='static\images\square1.png', message=msg)
        except:
            return template('approxim_2deg.tpl', title='Аппроксимация 2-й ст.', image_data='static\images\graph_strt.png', message=err_msg)
    else:
        num_elements = 5  # Заданное количество элементов
        x = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=float)
        y = np.array([random.uniform(0.0, 100.0) for _ in range(num_elements)], dtype=float) 

        # Основные вычисления
        A = np.vstack([x**2, x, np.ones(len(x))]).T
        k, b, c = np.linalg.lstsq(A, y, rcond=None)[0]
        y_pred = k*x**2 + b*x + c
        r2 = r2_score(y, y_pred) 

        # построение графика
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.plot(x, y, 'o', label='Исходные данные', markersize=5)
        ax.plot(x, k * x**2 + b * x, 'r', label='Приближенная линия')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend()
        ax.grid(True)

        plt.savefig('static/images/square2.png', dpi=300, bbox_inches='tight') #сохранение построенного графика

        msg='X = {}; Y = {} \nКоэффициенты квадратичной линии регрессии: a0={}, a1={} a2={} \nКоэффициент детерминированности R2={}'.format(x, y.round(), k.round(), b.round(), c.round(), r2.round())
        # Возвращает темплейт
        return template('approxim_2deg.tpl', title='Аппроксимация 2-й ст.', image_data='static\images\square2.png', message=msg)