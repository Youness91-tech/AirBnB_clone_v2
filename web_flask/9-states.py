#!/usr/bin/python3
"""Starts a Flask web application:
    - web application must be listening on 0.0.0.0, port 5000
    - Routes:
        - /states: display a HTML page: (inside the tag BODY)
            - H1 tag: "States"
            - UL tag: with the list of all State objects present in DBStorage
            sorted by name (A->Z) tip
                - LI tag: description of one State: <state.id>:
                    <B><state.name></B>
        - /states/<id>: display a HTML page: (inside the tag BODY)
            - H1 tag: "State"
            - H3 tag: "Cities:"
            - UL tag: with the list of City objects linked to the State sorted
            by name (A->Z)
                - LI tag: description of one City: <city.id>:
                    <B><city.name></B>
"""
from flask import Flask
from flask import render_template
from models import *
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_list(id=None):
    """display HTML page: (inside the tag BODY)"""
    states = storage.all('State')
    if id is not None:
        id = 'State.' + id
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def teardown_db(exception):
    """remove current sqlalchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
