from bottle import route, run, request, template
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

@route('/approx1', method='POST')
def approx1():
    x = np.array(request.forms.get('X').split(), dtype=float)
    y = np.array(request.forms.get('Y').split(), dtype=float)

    # Calculate the coefficients using the method of least squares
    A = np.vstack([x, np.ones(len(x))]).T
    k, b = np.linalg.lstsq(A, y, rcond=None)[0]

    # Generate the graph
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.plot(x, y, 'o', label='Original data', markersize=5)
    ax.plot(x, k*x + b, 'r', label='Fitted line')
    ax.legend()
    plt.savefig('static/images/graph.png', dpi=300, bbox_inches='tight')

    # Render the template with the coefficients and graph
    return template('approxim_1deg', title='linear', year=datetime.now().year, k=k, b=b)