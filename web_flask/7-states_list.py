#!/usr/bin/python3
from flask import Flask
from models import storage
from models import State
from flask import render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def show_states_list():
    """gets states lists"""
    states = storage.all('State')
    return render_template('7-states_list.html', state=state)


@app.teardown_appcontext
def tear_down_db(n):
    """ sql session closes """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
