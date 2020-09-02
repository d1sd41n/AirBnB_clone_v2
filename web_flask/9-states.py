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


@app.route('/states/', strict_slashes=False)
def states_list():
    """list states"""
    states = storage.all(State)
    render = render_template('9-states.html', states=states)
    return render


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """search one state by id and display it
    """
    states = storage.all(State).values()
    found = False
    for i in states:
        if i.id == id:
            found = True
            break
    if found:
        return render_template("9-states.html", state=i)
    else:
        return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """closes etorage"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
