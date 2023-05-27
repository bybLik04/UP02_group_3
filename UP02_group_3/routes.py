"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/authors')
@view('authors')
def authors():
    """Renders the authors page."""
    return dict(
        title='authors',
        message='Your authors page.',
        year=datetime.now().year
    )
