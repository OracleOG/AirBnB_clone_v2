#!/usr/bin/env python3
""" Python script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greetings():
    return "<p>Hello HBNB</p>"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
