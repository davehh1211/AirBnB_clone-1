#!/usr/bin/python3
"""displays a default template
    """
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def fetchstorage():
    """fetching data"""
    states = list(storage.all(State).values())
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """fetching data from cities"""
    states = list(storage.all(State).values())
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def stateid(id=None):
    """state by id"""
    states = storage.all(State)
    if id is not None:
        id = 'State.' + id
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def db_teardown(exception):
    """[summary]"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
