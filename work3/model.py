from flask_sqlalchemy import SQLAlchemy

bd = SQLAlchemy()


class User(bd.Model):
    id = bd.Column(bd.Integer, primary_key=True)
    first_name = bd.Column(bd.String(20), unique=True, nullable=False)
    second_name = bd.Column(bd.String(20), unique=True, nullable=False)
    email = bd.Column(bd.String(30), unique=True, nullable=False)
    password = bd.Column(bd.String(15), unique=True, nullable=False)


