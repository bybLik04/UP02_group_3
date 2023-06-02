from bottle import route, run, request, template, post
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

@post('/approx1', method='POST')
def approx1():
    if request.forms.get('deg1_btn'):
        try:
            # Получение коэффициентов из формы
            x = np.array(request.forms.get('X').split(), dtype=float)
            y = np.array(request.forms.get('Y').split(), dtype=float)

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
            
            A = np.vstack([x, np.ones(len(x))]).T
            k, b = np.linalg.lstsq(A, y, rcond=None)[0]
            y_pred = k*x + b
            r2 = r2_score(y, y_pred)

            # построение графика
            fig, ax = plt.subplots(figsize=(3, 3))
            ax.plot(x, y, 'o', label='Original data', markersize=5)
            ax.plot(x, k*x + b, 'r', label='Fitted line')
            ax.legend()
            plt.savefig('static/images/graph5.png', dpi=300, bbox_inches='tight')

            # Возвращает темплейт
            if trigg != True:
                return template('approxim_1deg.tpl', title='linear', image_data='static\images\graph5.png',year=datetime.now().year, k= 'err', b= 'err', r = 'err', ex ='Ошибка входных данных!! ')
            else:
                return template('approxim_1deg.tpl', title='linear', image_data='static\images\graph5.png',year=datetime.now().year, k=k.round(), b=b.round(), r = r2.round(), ex = '')
        except:
            return template('approxim_1deg.tpl', title='linear', image_data='static\images\graph5.png',year=datetime.now().year, k= 'err', b= 'err', r = 'err', ex ='Ошибка входных данных!! ')
    else:
        x = np.array("1 3 5 6 7".split(), dtype=float)
        y = np.array("3 6 3 5 2".split(), dtype=float)

            # Основные вычисления
        A = np.vstack([x, np.ones(len(x))]).T
        k, b = np.linalg.lstsq(A, y, rcond=None)[0]
        y_pred = k*x + b
        r2 = r2_score(y, y_pred)

            # построение графика
        fig, ax = plt.subplots(figsize=(3, 3))
        ax.plot(x, y, 'o', label='Original data', markersize=5)
        ax.plot(x, k*x + b, 'r', label='Fitted line')
        ax.legend()
        plt.savefig('static/images/graph5.png', dpi=300, bbox_inches='tight')

            # Возвращает темплейт
        return template('approxim_1deg.tpl', title='linear', image_data='static\images\graph5.png',year=datetime.now().year, k=k.round(), b=b.round(), r = r2.round(), ex = 'Пример: x - [1 3 5 6 7], y - [3 6 3 5 2], ')