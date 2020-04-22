#!/usr/bin/python3
from flask import Flask
from models import storage
from models import State
from flask import render_template


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """gets states lists"""
    state_list = storage.all('State')
    return render_template('7-states_list.html', state_list=state_list)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def tear_down_db(n):
    """ sql session closes """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
