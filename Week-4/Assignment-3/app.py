from flask import Flask, request, render_template
from flask import make_response, redirect, url_for, flash
import pymysql.cursors

app = Flask(__name__)
app.secret_key = '4fu7k84k54tu646ed'


def create_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='2827ABcd',
        database='assignment',
        cursorclass=pymysql.cursors.DictCursor
    )

DEBUG = True
PORT = 4000
HOST = '0.0.0.0'


@app.route("/home")
def home():
    create_connection()
    return render_template("home.html")


@app.route("/sign_in", methods=['GET'])
def sign_in():
    parameters = request.args
    email_get = parameters.get('email')
    password_get = parameters.get('password')


    with create_connection() as connection:
        with connection.cursor() as cursor:
            sql = "SELECT `email`, `password` FROM `user` WHERE `email`=%s AND `password`=%s"
            cursor.execute(sql, (email_get, password_get))
            result = cursor.fetchone()

            success = False
            if result:
                success = True

        connection.commit()

    if success == True:
        return render_template("member.html")
    else:
        flash('Try Sign In Again', 'success')
        return redirect(url_for("home"))



@app.route("/sign_up", methods=['GET'])
def sign_up():
    parameters = request.args
    email_get = parameters.get('email')
    password_get = parameters.get('password')


    with create_connection() as connection:
        with connection.cursor() as cursor:
            sql = "SELECT `email` FROM `user` WHERE `email`=%s"
            cursor.execute(sql, (email_get,))
            result = cursor.fetchone()

            # Create a new record if no existing row
            success = False
            if result is None:
                sql = "INSERT INTO `user` (`email`, `password`) VALUES (%s, %s)"
                cursor.execute(sql, (email_get, password_get))
                success = True

        connection.commit()

    if success == True:
        return render_template("member.html")
    else:
        flash('Try Sign Up Again', 'success')
        return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
