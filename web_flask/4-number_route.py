#!/usr/bin/python3

"""
    This Python Flask app defines a route that returns 'Hello HBNB!'
    when the root URL is accessed.
    :return: The code defines a Flask route at the root URL ('/')
    with the function `hello_hbnb()` that
    returns the string 'Hello HBNB!'. When a user accesses
    the root URL of the Flask application, the
    message 'Hello HBNB!' will be returned as the response.
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '%d is a number' % n


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
