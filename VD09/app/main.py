from flask import (
    Blueprint, 
    render_template, 
    redirect, 
    url_for, 
    flash
)
from flask_login import login_required, current_user
from datetime import datetime

from app.extensions import db
from app.models import UserAction

import sqlalchemy as sa

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/profile')
@login_required
def profile():
    clicks = {
        'total': 0, 
        'last': datetime.min,
        'user': current_user.username
        }
    last_action = current_user.actions.order_by(UserAction.timestamp.desc()).first()

    if last_action:
        clicks['total'] = current_user.clicks
        clicks['last'] = last_action.timestamp

    return render_template('profile.html', clicks=clicks)

@main_bp.route('/click', methods=['POST'])
@login_required
def click():
    print('click')
    new_action = UserAction(user_id=current_user.id)

    current_user.clicks += 1

    db.session.add(new_action)
    db.session.commit()

    flash('Клик!')

    return redirect(url_for('main.profile'))