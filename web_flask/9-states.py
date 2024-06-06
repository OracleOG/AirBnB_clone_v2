#!/usr/bin/python3
''' Script thst runs an app with flask '''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def list_states():
    ''' Function called through the / route '''
    state_dict = storage.all(State)
    return render_template('7-states_list.html', states=state_dict)


@app.route("/states/<id>", strict_slashes=False)
def list_states_id(id):
    ''' Function called through the / route '''
    state_dict = storage.all(State)
    state_list = []
    for value in state_dict.values():
        if value.id == id:
            state_list.append(value)

    return render_template('9-states.html', states=state_list[0])


@app.teardown_appcontext
def teardown_db(exception):
    """Method to handle app context teardown."""
    storage.close()



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
