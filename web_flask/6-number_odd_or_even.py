#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """
    display “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
    display "HBNB"
    """
    return "HBNB"


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
