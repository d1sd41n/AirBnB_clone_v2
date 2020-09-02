#!/usr/bin/python3
"""ruens flask
"""
import re
from models.state import State
from models.city import City
from flask import render_template
from models import storage
from collections import OrderedDict
from flask import Flask

app = Flask(__name__)


@app.route('/cities_by_states/', strict_slashes=False)
def cities_by_states():
    """list states"""
    states = storage.all(State)
    render = render_template('8-cities_by_states.html', states=states)
    return render


@app.teardown_appcontext
def teardown(exc):
    """closes etorage"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
