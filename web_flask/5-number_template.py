#!/usr/bin/python3
"""displays a default template
    """
from flask import Flask, render_template

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
    """displays C is <text>"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def pythonfun(text='is cool'):
    """[summary]
    Args:
    text ([type]): [description]
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def integer(n):
    """only integers
    """
    return '{:d} is a number'.format(n)


@app.route('/number_template/<n>', strict_slashes=False)
def numbertemplate(n):
    """[summary]"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
