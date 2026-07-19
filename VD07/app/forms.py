from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import sqlalchemy as sa
from app.models import User
from app import db
from flask_login import current_user

class RegistrationForm(FlaskForm):
    name = StringField('Имя пользователя', validators=[DataRequired(), Length(min=2, max=35)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердить пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    def validate_name(self, name):
        user = db.session.scalar(sa.select(User).where(User.name == name.data))
        if user:
            raise ValidationError('Это имя пользователя уже занято. Пожалуйста, выберите другое.')
        
    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(User.email == email.data))
        if user:
            raise ValidationError('Этот email уже зарегистрирован. Пожалуйста, выберите другой.')
        
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

class UpdateProfileForm(FlaskForm):
    name = StringField('Имя пользователя', validators=[DataRequired(), Length(min=2, max=35)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    # Пароли не обязательны. Пользователь заполняет их, только если хочет сменить
    password = PasswordField('Новый пароль (оставьте пустым, если не меняете)')
    confirm_password = PasswordField('Подтвердите новый пароль', validators=[EqualTo('password', message='Пароли должны совпадать')])
    submit = SubmitField('Обновить профиль')

    def validate_name(self, name):
        # Проверяем уникальность, только если пользователь изменил свое текущее имя
        if name.data != current_user.name:
            user = db.session.scalar(sa.select(User).where(User.name == name.data))
            if user:
                raise ValidationError('Это имя пользователя уже занято.')

    def validate_email(self, email):
        # Проверяем уникальность, только если пользователь изменил свой текущий email
        if email.data != current_user.email:
            user = db.session.scalar(sa.select(User).where(User.email == email.data))
            if user:
                raise ValidationError('Этот email уже используется.')    