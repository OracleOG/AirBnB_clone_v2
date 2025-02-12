#!/usr/bin/python3
''' Script thst runs an app with flask '''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def list_states():
    ''' Function called through the / route '''
    state_dict = storage.all(State)
    city_dict = storage.all(City)
    return render_template('8-cities_by_states.html', states=state_dict, cities=city_dict)


@app.teardown_appcontext
def teardown_db(exception):
    """Method to handle app context teardown."""
    storage.close()



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
