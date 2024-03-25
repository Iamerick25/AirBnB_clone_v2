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
    displays custom text
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
    display text if ONLY n is a number
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """
    display HTML page
    """
    return render_template("5-number.html", number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
