#!/usr/bin/python3
"""
<<<<<<< HEAD
    Sript that starts a Flask web application
 """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbn():
    """
        function to return Hello HBNB!
=======
script that starts a Flask web application
"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    display “Hello HBNB!”
>>>>>>> f36534d4a39c1f0dec90ab7d46d53d3726ca7954
    """
    return "Hello HBNB!"


<<<<<<< HEAD
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        function to return HBNB
    """
    return "HBNB"
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
=======
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    display "HBNB"
    """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
>>>>>>> f36534d4a39c1f0dec90ab7d46d53d3726ca7954
