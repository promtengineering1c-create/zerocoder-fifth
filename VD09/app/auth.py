from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required

from app.extensions import db
from app.forms import RegistrationForm, LoginForm
from app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.profile'))

    form = RegistrationForm()

    if form.validate_on_submit():
        new_user = User(username=form.username.data)
        new_user.set_password(form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash('Вы зарегистрированы!', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html', title='Регистрация', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.profile'))

    form = LoginForm()

    if form.validate_on_submit():
        user = db.session.scalar(db.select(User).where(User.username == form.username.data))

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.profile'))
        else:
            flash('Неверный логин или пароль', 'danger')
            return redirect(url_for('auth.login'))

    return render_template('login.html', title='Вход', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

    
