from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

import sqlalchemy as sa
from app.models import User
from app.extensions import db

class RegistrationForm(FlaskForm):

    username = StringField('Логин', validators=[DataRequired(message='Логин обязателен'), Length(min=3, max=35, message='Длина логина должна быть от 3 до 35 символов')])

    password = PasswordField('Пароль', validators=[DataRequired(message="Пароль обязателен"), Length(min=8, max=20, message='Длина пароля должна быть от 8 до 20 символов')])

    confirm_password = PasswordField('Подтвердить пароль', validators=[DataRequired(), EqualTo('password', message='Пароли должны совпадать')])

    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user:
            raise ValidationError('Это имя уже занято. Выберите другое.')

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(message='Логин обязателен'), Length(min=3, max=35, message = 'Имя должно быть от 3 до 35 символов')])

    password = PasswordField('Пароль', validators=[DataRequired(message="Введите пароль"), Length(min=8, max=20, message = 'Пароль должен быть от 8 до 20 символов')])

    remember = BooleanField('Запомнить меня')

    submit = SubmitField('Войти')
