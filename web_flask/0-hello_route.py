#!/usr/bin/python3
"""This is a script that starts a Flask web application"""

from flask import Flask

App = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_HBNB():
    return "Hello HBNB!"


if __name__ == "__main__":
    App.run(host='0.0.0.0', port=5000)
