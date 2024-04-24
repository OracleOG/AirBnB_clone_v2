#!/usr/bin/python3
''' Script thst runs an app with flask '''
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    ''' Function called through the / route '''
    return "Hello, HBNB!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
