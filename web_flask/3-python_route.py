#!/usr/bin/python3
"""
Script that starts a Flask web application:
Listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route("/", strict_slashes=False)
def hello():
    """Return string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Return string"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """display C + text variable"""
    return "C {}".format(text.replace("_", " "))

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """display Python + text variable"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
