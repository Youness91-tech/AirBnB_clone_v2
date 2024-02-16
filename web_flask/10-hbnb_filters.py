#!/usr/bin/python3
"""Starts a Flask web application:
    - web application must be listening on 0.0.0.0, port 5000
    - Routes:
        - /hbhb_filters: display a HTML page: (inside the tag BODY)      
"""
from flask import Flask
from flask import render_template
from models import *
from models import storage


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """display HTML page: (inside the tag BODY)"""
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """remove current sqlalchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
