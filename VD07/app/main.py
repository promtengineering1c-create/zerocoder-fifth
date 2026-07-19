from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.forms import UpdateProfileForm
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

# НОВЫЙ МАРШРУТ
@main.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = UpdateProfileForm()
    
    if form.validate_on_submit():
        # Обновляем данные текущего пользователя
        current_user.name = form.name.data
        current_user.email = form.email.data
        
        # Если поле пароля не пустое, хешируем и сохраняем новый пароль
        if form.password.data:
            current_user.set_password(form.password.data)
            
        # Сохраняем изменения в базу данных
        db.session.commit()
        
        flash('Ваш профиль был успешно обновлен!', 'success')
        return redirect(url_for('main.profile'))
        
    elif request.method == 'GET':
        # Если это просто открытие страницы (GET-запрос), предзаполняем поля текущими данными
        form.name.data = current_user.name
        form.email.data = current_user.email
        
    return render_template('edit_profile.html', form=form)