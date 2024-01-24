from flask import Flask, request


app = Flask(__name__)

DEBUG = True
PORT = 3000
HOST = '0.0.0.0'


def sum(num):
    if num == 0:
        return 0
    return sum(num-1) + num


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/data", methods=['GET'])
def lack_parameter():
    parameters = request.args
    number_value = parameters.get('number')
    print(number_value)
    if number_value is None:
        return "<p>Lack of Parameter</p>"

    if not isinstance(int(number_value), int):
        return "<p> Wrong Parameter</p>"
    else:
        total = sum(int(number_value))
        return f"<p>{ total }</p>"


if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
