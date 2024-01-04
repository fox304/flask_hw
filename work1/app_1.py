"""
Задание

Создать базовый шаблон для интернет-магазина,
содержащий общие элементы дизайна (шапка, меню, подвал),
и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
Например, создать страницы
«Одежда», «Обувь» и «Куртка», используя базовый шаблон.


"""

from flask import Flask,render_template

app = Flask(__name__)


@app.route('/1/')
def shop():
    context = {'title': 'Одежда'}
    return render_template('clothes.html',**context)


@app.route('/2/')
def shop2():
    context = {'title': 'Куртки'}
    return render_template('jackets.html',**context)


@app.route('/3/')
def shop3():
    context = {'title': 'Обувь'}
    return render_template('shoes.html',**context)


app.run(port=8000)
