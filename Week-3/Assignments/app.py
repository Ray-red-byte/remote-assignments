from flask import Flask, request, render_template
from flask import make_response, redirect, url_for

import json


app = Flask(__name__)

DEBUG = True
PORT = 3000
HOST = '0.0.0.0'


def sum(num):
    if num == 0:
        return 0
    return sum(num-1) + num


def get_cookies():
    try:
        data = json.loads(request.cookies.get('name'))
        print(data)
    except TypeError:
        data = ""
    return data


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/sum.html")
def sum_page():
    return render_template("sum.html")


@app.route("/myName")
def check_name():
    name = get_cookies()
    return render_template("myName.html", name=name)


@app.route("/trackName", methods=['GET'])
def set_name_cookies():
    parameters = request.args
    name_get = parameters.get('name')

    # Add into cookies
    response = make_response(redirect(url_for('check_name')))
    response.set_cookie('name', json.dumps(name_get))
    return response


@app.route("/data", methods=['GET'])
def lack_parameter():
    parameters = request.args
    number_value = parameters.get('number')
    if number_value is None:
        return "<p>Lack of Parameter</p>"

    try:
        total = sum(int(number_value))
        return f"<p>{ total }</p>"
    except ValueError:
        return "<p> Wrong Parameter</p>"


if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
