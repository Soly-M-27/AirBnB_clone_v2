#!/usr/bin/python3
''' script that starts a Flask web application '''

from flask import Flask
from models import storage, storage.all(...)


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
    ''' If n is an int, display HTML page with n variable in it'''
    if n is int:
        index = open("5-number.html", 'r')
        s = index.read().format(n)
        return "{}".format(n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    ''' Display number is even or odd '''
    if n / 2 == 0:
        index = open("6-number_odd_or_even.html", 'r')
        s = index.read().format(n, OorE='is even')
        return s
    else:
        index = open("6-number_odd_or_even.html", 'r')
        s = index.read().format(n, OorE='is odd')
        return s


@app.teardown_appcontext
@app.route('/states_list', strict_slashes=False)
def display_states(state.id, state.name):
    ''' Display States with ID and names '''
    index = open("7-states_list.html", 'r')
    s = index.read().format("States", state.id, state.name)
    storage.close()
    return s


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
