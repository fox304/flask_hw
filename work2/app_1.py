"""
Задание

Создать страницу, на которой будет форма для ввода имени и электронной почты,
при отправке которой будет создан cookie-файл с данными пользователя,
а также будет произведено перенаправление на страницу приветствия,
 где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка «Выйти»,
при нажатии на которую будет удалён cookie-файл с данными пользователя
и произведено перенаправление на страницу ввода имени и электронной почты.
"""

from flask import Flask,render_template
import secrets

app = Flask(__name__)
secret_code = secrets.token_hex()


@app.route("/")
def input_():
    return render_template("input.html")


@app.route("/greeting/")
def greeting():
    return render_template("greeting.html")

app.run()