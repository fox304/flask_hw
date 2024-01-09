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

from flask import Flask,render_template,make_response,request,url_for,redirect

app = Flask(__name__)


@app.get("/")
def get_():
    return render_template("input.html")


@app.post("/")
def post_():
    response = make_response(render_template("input.html"))
    name = request.form['us_name']
    mail = request.form['el_mail']
    response.set_cookie('us',name)
    response.set_cookie('el',mail)
    return redirect(url_for("greeting",name=name))


@app.route("/greeting/<string:name>")
def greeting(name):
    return render_template("greeting.html",name=name)


app.run(debug=True)
