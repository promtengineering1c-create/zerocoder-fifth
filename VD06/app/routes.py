from flask import render_template, redirect, url_for, request
from app import app

users = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        hobby = request.form['hobby']
        age = request.form['age']
        if name and city and hobby and age:
            user = {
                'name': name,
                'city': city,
                'hobby': hobby,
                'age':age
            }
            users.append(user)
            return redirect(url_for('index'))
    return render_template('users.html', users=users)