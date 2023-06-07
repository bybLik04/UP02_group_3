from bottle import route, run, request, template, post
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

def calculate_linear_regression(x, y):
    A = np.vstack([x, np.ones(len(x))]).T
    k, b = np.linalg.lstsq(A, y, rcond=None)[0]
    y_pred = k * x + b
    r2 = r2_score(y, y_pred)
    return k.round(), b.round(), r2.round()

def plot_graph(x, y, k, b):
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.plot(x, y, 'o', label='Original data', markersize=5)
    ax.plot(x, k * x + b, 'r', label='Fitted line')
    ax.legend()
    plt.savefig('static/images/graph5.png', dpi=300, bbox_inches='tight')

@post('/approx1', method='POST')
def approx1():
    req = request.forms.get('deg1_btn')
    try:
        x = np.array(request.forms.get('X').split(), dtype=float)
        y = np.array(request.forms.get('Y').split(), dtype=float)
        if not req:
            x = np.array("1 3 5 6 7".split(), dtype=float)
            y = np.array("3 6 3 5 2".split(), dtype=float)
        
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

        if trigg:
            k, b, r2 = calculate_linear_regression(x, y)
            plot_graph(x, y, k, b)
            return template('approxim_1deg.tpl', title='linear', image_data='static\images\graph5.png', year=datetime.now().year, k=k, b=b, r=r2, ex='')
        else:
            return template('approxim_1deg.tpl', title='linear', image_data='static\images\graph5.png', year=datetime.now().year, k='err', b='err', r='err', ex='Ошибка входных данных!!')
    except:
        return template('approxim_1deg.tpl', title='linear', image_data='static\images\graph_.png', year=datetime.now().year, k='err', b='err', r='err', ex='Ошибка входных данных!!')

