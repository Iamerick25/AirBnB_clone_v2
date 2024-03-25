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
app.url_map.strict_slashes = False


@app.route("/")
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
=======
@app.route("/hbnb")
def hbnb():
    """
    display "HBNB"
>>>>>>> f36534d4a39c1f0dec90ab7d46d53d3726ca7954
    """
    return "HBNB"


<<<<<<< HEAD
@app.route('/c/<text>', strict_slashes=False)
def text_var(text):
    """
        function to display text variable passed in
    """
    return "C {}".format(text.replace("_", " "))
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
=======
@app.route("/c/<text>")
def c_route(text):
    """
    displays custom text
    """
    return "C {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
>>>>>>> f36534d4a39c1f0dec90ab7d46d53d3726ca7954
