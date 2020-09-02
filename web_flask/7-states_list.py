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


@app.route('/states_list/', strict_slashes=False)
def states_list():
    """list states"""
    states = storage.all(State)
    render = render_template('7-states_list.html', states=states)
    return render


@app.teardown_appcontext
def teardown(exc):
    """closes etorage"""
    storage.close()


if __name__ == '__main__':
    app.run()
