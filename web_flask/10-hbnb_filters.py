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
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def states_list():
    """list states"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    render = render_template('10-hbnb_filters.html',
                             states=states,
                             amenities=amenities
                             )
    return render


@app.teardown_appcontext
def teardown(exc):
    """closes etorage"""
    storage.close()


if __name__ == '__main__':
    app.run()
