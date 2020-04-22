#!/usr/bin/python3
from flask import Flask
from models import storage
from models import State
from flask import render_template


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """gets states lists"""
    state_list = storage.all('State')
    return render_template('7-states_list.html', state_list=state_list)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    s_list = storage.all('State')
    s_id = []
    for states in s_list.values():
        if id == states.id:
            s_id = states

    return render_template('9-states.html', s_list=s_list, s_id=s_id)


@app.teardown_appcontext
def tear_down_db(n):
    """ sql session closes """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
