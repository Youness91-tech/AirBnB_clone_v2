#!/usr/bin/python3
"""Starts a Flask web application:
    - web application must be listening on 0.0.0.0 port 5000
    - Routes:
        - /cities_by_states: display HTML page: (inside the tag BODY)
            - H1 tag: "States"
            - UL tag: with the list of all State objects present in DBStorage
            sorted by name (A->Z) tip
                - LI tag: description of one State: <state.id>:
                    <B><state.name></B>
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """display HTML page: (inside the tag BODY)"""
    states = storage.all(State)
    states = dict(sorted(states.items(), key=lambda item: item[1].name))
    # for k, v in states.items():
    #     print("{}: {}".format(k, v.name))
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """remove current sqlalchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
