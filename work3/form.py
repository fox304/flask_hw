from wtforms import StringField,PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Email,Length,EqualTo


class Checking(FlaskForm):
    first = StringField("Имя_пользователя", validators=[DataRequired()])
    second = StringField("Фамилия_пользователя", validators=[DataRequired()])
    mail = StringField("Почта", validators=[DataRequired(), Email()])
    passw = PasswordField("Пароль", validators=[DataRequired(),Length(min=8)])
    passw2 = PasswordField("Пароль подтверждение",
                           validators=[DataRequired(),EqualTo('passw')])
