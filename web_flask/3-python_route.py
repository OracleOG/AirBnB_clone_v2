from flask import Flask
''' Script thst runs an app with flask'''

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    ''' Function called through the / route '''
    return "Hello, HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_HBNB():
    ''' Function called through the /hbnb route '''
    return "HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def welcome_c(text):
    ''' Function called through the /hbnb/c/<var> route '''
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route("/python/<value>", strict_slashes=False)
def welcome_python(value):
    ''' Function called through the /hbnb/python/<var> route '''
    value = value.replace('_', ' ')
    return f"Python {value}"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
