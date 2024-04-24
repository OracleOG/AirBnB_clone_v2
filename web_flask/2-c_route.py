#!/usr/bin/python3
''' Script thst runs an app with flask'''
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    ''' Function called through the / route '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_HBNB():
    ''' Function called through the /hbnb route '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def welcome_c(text):
    ''' Function called through the /hbnb/c/<var> route '''
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
