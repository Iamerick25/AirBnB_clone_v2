#!/usr/bin/python3
"""
<<<<<<< HEAD
    Sript that starts a Flask web application
 """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbn():
    """
        function to return Hello HBNB!
=======
script that starts a Flask web application
"""

from flask import Flask, render_template


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


@app.route('/python/<text>', strict_slashes=False)
def text_var_python(text="is cool"):
    """
        function to display text variable, with default "is cool"
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def var_num(n):
        """
             function to display a variable, but only if an int
        """
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def var_num_template(n):
        """
            function to display number in html page
        """
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def var_num_even_odd(n):
        """
            function to display even or odd number
        """
        return render_template("6-number_odd_or_even.html", n=n)
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
=======
@app.route("/c/<text>")
def c_route(text):
    """
    displays custom text, replaces '_' with ' '
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python")
@app.route("/python/<text>")
def python_route(text='is cool'):
    """
    displays custom text
    display default text
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>")
def number(n):
    """
    display text
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """
    render HTML template page if n is int
    """
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """
    render HTML template page
    """
    value = ""
    if n % 2 == 0:
        value = "even"
    else:
        value = "odd"

    return render_template("6-number_odd_or_even.html", number=n, value=value)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
>>>>>>> f36534d4a39c1f0dec90ab7d46d53d3726ca7954
