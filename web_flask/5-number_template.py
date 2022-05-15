#!/usr/bin/python3
''' script that starts a Flask web application '''

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    ''' display "Hello HBNB!" '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' display "HBNB" '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    ''' display "C " + text '''
    new_text = text.replace("_", " ")
    return "C {}".format(new_text)


@app.route('/python', strict_slashes=False)
@app.route('/python/(<text>)', strict_slashes=False)
def python_text(text='is cool'):
    ''' display "Python " + text=(default)"is cool" '''
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    ''' Display n if n is an integer'''
    if n is int:
        return ("{:d} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_tem(n):
    if n is int:
        index = open("5-number.html", 'r')
        s = index.read().format(n)
        return s


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
