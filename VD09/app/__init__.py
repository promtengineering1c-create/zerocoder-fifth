from flask import Flask
from app.extensions import db, bcrypt, login_manager, migrate
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return db.session.get(User, int(user_id))

    with app.app_context():
        from app.auth import auth_bp as auth_bp
        app.register_blueprint(auth_bp)

        from app.main import main_bp as main_bp
        app.register_blueprint(main_bp)

    return app
