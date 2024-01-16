"""
Создать форму для регистрации пользователей на сайте.
Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль"
и кнопку "Зарегистрироваться".
При отправке формы данные должны сохраняться в базе данных,
а пароль должен быть зашифрован.
"""

from flask import Flask,render_template,redirect,url_for
from flask_wtf import CSRFProtect
from secrets import token_hex
from hashlib import sha256
from model import User,bd
from form import Checking

app = Flask(__name__)
app.config["SECRET_KEY"] = token_hex()
csrf = CSRFProtect(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database_for_homework3.db"
bd.init_app(app)


@app.route("/",methods=["POST","GET"])
def fill_form():
    form = Checking()
    if form.validate_on_submit():
        user = User(email=form.mail.data,
                    first_name=form.first.data,
                    second_name=form.second.data,
                    password=sha256(form.passw.data.encode(encoding='utf-8')).hexdigest())
        bd.session.add(user)
        bd.session.commit()
        return redirect(url_for('fill_form'))

    return render_template("index.html", form=form)


@app.cli.command("create")
def create_bd():
    bd.create_all()
    print("ура, мы создали базу данных!!!")


if __name__ == '__main__':
    app.run()
