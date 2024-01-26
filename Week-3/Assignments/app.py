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
    except TypeError:
        data = {'name': []}
    return data


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/sum.html")
def sum_page():
    return render_template("sum.html")


@app.route("/<myName>")
def check_name(myName):
    names = get_cookies()
    username = myName
    return render_template("myName.html", names=names, username=username)


@app.route("/trackName", methods=['GET'])
def set_name_cookies():
    parameters = request.args
    name_get = parameters.get('name')
    names = get_cookies()

    # Add into cookies
    names['name'].append(name_get)
    print(names)
    response = make_response(redirect(url_for('check_name', myName=name_get)))
    response.set_cookie('name', json.dumps(names))
    return response


@app.route("/data", methods=['GET'])
def lack_parameter():
    parameters = request.args
    number_value = parameters.get('number')
    if number_value is None:
        return "<p>Lack of Parameter</p>"

    if not isinstance(int(number_value), int):
        return "<p> Wrong Parameter</p>"
    else:
        total = sum(int(number_value))
        return f"<p>{ total }</p>"


if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
