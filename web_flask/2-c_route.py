#!/usr/bin/python3
"""displays a default template
    """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def appflask():
    """ displays the path by default"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def index2():
    """displays another route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cdisplay(text):
    """[summary]"""
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
