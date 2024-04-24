#!/usr/bin/python3
"""
    A python script that starts a Flask application:
    Requirements:
    - You must use the option strict_slashes=False in your route definition
    Routes:
    -  /: display “Hello HBNB!”
    - /hbnb: display “HBNB”
    - /c/<text>: display “C ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )
    - /python/(<text>): display “Python ”, followed by the value of the text
    variable (replace underscore _ symbols with a space).
    Note: default value of text="is cool"
    - /number/<n>: display “n is a number” only if n is an integer
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
    replaced_text = text.replace('_', ' ')
    return f"C {replaced_text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    replaced_text = text.replace('_', ' ')
    return f"Python {replaced_text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
