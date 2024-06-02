#!/usr/bin/python3
''' Script thst runs an app with flask '''
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def world():
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def is_fun(text):
    text = text.replace("_"," ")
    return "C {}".format(text)


@app.route('/python/', strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def is_cool(text="is cool"):
    text = text.replace("_"," ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def is_num(n):
    return "n is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def temp_num(n):
    return render_template('5-number.html', num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_or_odd(n):
    return render_template('6-number_odd_or_even.html', number=n)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

