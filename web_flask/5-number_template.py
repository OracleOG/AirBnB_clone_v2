#!/usr/bin/python3
''' Script thst runs an app with flask'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    ''' Function called through the / route '''
    return "Hello, HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_HBNB():
    ''' Function called through the /hbnb route '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def welcome_c(text):
    ''' Function called through the /hbnb/c/<var> route '''
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """ Function called with /python/<text> route """
    if text != 'is cool':
        text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Function called with /number/<n> route """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_number(n):
    """ Function called with /number/<n> route """
    return render_template('5-number.html', num=n)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
