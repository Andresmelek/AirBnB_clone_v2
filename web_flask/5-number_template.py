#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ returns hello"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """ returns hbnb """
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    """ c is fun for craps """
    complement = text.replace("_", " ")
    return 'C %s' % complement


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def show_python_is_cool(text):
    """ python is likeable """
    complement = text.replace("_", " ")
    return 'Python %s' % complement


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ displays only if it is an integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ displays template if it is an integer """
    return num_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
