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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
