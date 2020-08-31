#!/usr/bin/python3
"""runs flask
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    return "C " + " ".join(text.split("_"))

if __name__ == '__main__':
    app.run()
