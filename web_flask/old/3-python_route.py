#!/usr/bin/python3
"""
    A python script thaat starts a Flask application:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text variable
    (replace underscore _ symbols with a space) - default value of C is 'cool'
    /python/<text>: display “Python ”, followed by the value of the text
    variable (replace underscore _ symbols with a space)
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    # replace underscore with space
    replaced_text = text.replace('_', ' ')
    return f"C {replaced_text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    # replace underscore with space
    replaced_text = text.replace('_', ' ')
    return f"Python {replaced_text}"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
