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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)