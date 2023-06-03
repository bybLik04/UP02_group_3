import random
from bottle import request, template, post
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

@post('/approx2', method='POST')
def approx2():
    if request.forms.get('dg2_btn'):
        try:
            err_msg='Ошибка входных данных!'

            # Получение коэффициентов из формы
            x_arr = np.array(request.forms.get('X').split(), dtype=float)
            y_arr = np.array(request.forms.get('Y').split(), dtype=float)

            # Объединение массивов x и y в список пар
            combined = list(zip(x_arr, y_arr))

            # Сортировка списка пар по возрастанию значений x
            combined.sort(key=lambda pair: pair[0])

            # Разделение пар обратно на массивы x и y
            x_sorted, y_sorted = zip(*combined)

            # Преобразование обратно в массивы NumPy
            x = np.array(x_sorted)
            y = np.array(y_sorted)

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

            # Аппроксимация методом наименьших квадратов
            A = np.vstack([x**2, x, np.ones(len(x))]).T
            k, b, c = np.linalg.lstsq(A, y, rcond=None)[0]
            y_pred = k*x**2 + b*x + c
            r2 = r2_score(y, y_pred) #вычисление коэффициента детерминации

            # Построение графика
            fig, ax = plt.subplots(figsize=(5, 5))
            ax.plot(x, y, 'o', label='Исходные данные', markersize=5)
            ax.plot(x, k * x**2 + b * x + c, 'r', label='Приближенная линия')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.legend()
            ax.grid(True)
            plt.show()

            plt.savefig('static/images/square1.png', dpi=300, bbox_inches='tight') #сохранение построенного графика
            msg='Коэффициенты квадратичной линии регрессии: a0={}, a1={} a2={} \nКоэффициент детерминированности R2={}'.format(k.round(), b.round(), c.round(), r2.round())
            #msg='Коэффициенты квадратичной линии регрессии: {} \nКоэффициент детерминированности R2={}'.format(coefficients.round(), r2.round())

            # Возвращает темплейт
            if trigg != True:
                return template('approxim_2deg.tpl', title='Аппроксимация 2-й ст.', image_data='static\images\graph_strt.png', message=err_msg)
            else:
                return template('approxim_2deg.tpl', title='Аппроксимация 2-й ст.', image_data='static\images\square1.png', message=msg)
        except:
            return template('approxim_2deg.tpl', title='Аппроксимация 2-й ст.', image_data='static\images\graph_strt.png', message=err_msg)
    else:
        num_elements = 10  # Заданное количество элементов
        x_arr = np.array([random.uniform(0.0, 100.0) for _ in range(num_elements)], dtype=float)
        y_arr = np.array([random.uniform(0.0, 100.0) for _ in range(num_elements)], dtype=float) 
        # Объединение массивов x и y в список пар
        combined = list(zip(x_arr, y_arr))

        # Сортировка списка пар по возрастанию значений x
        combined.sort(key=lambda pair: pair[0])

        # Разделение пар обратно на массивы x и y
        x_sorted, y_sorted = zip(*combined)

        # Преобразование обратно в массивы NumPy
        x = np.array(x_sorted)
        y = np.array(y_sorted)

        # Аппроксимация методом наименьших квадратов
        A = np.vstack([x**2, x, np.ones(len(x))]).T
        k, b, c = np.linalg.lstsq(A, y, rcond=None)[0]
        y_pred = k*x**2 + b*x + c
        r2 = r2_score(y, y_pred)

        # Построение графика
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.plot(x, y, 'o', label='Исходные данные', markersize=5)
        ax.plot(x, k * x**2 + b * x + c, 'r', label='Приближенная линия')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend()
        ax.grid(True)
        plt.show()

        plt.savefig('static/images/square2.png', dpi=300, bbox_inches='tight') #сохранение построенного графика

        msg='X = {}; Y = {} \nКоэффициенты квадратичной линии регрессии: a0={}, a1={} a2={} \nКоэффициент детерминированности R2={}'.format(x.round(), y.round(), k.round(), b.round(), c.round(), r2.round())
        # Возвращает темплейт
        return template('approxim_2deg.tpl', title='Аппроксимация 2-й ст.', image_data='static\images\square2.png', message=msg)