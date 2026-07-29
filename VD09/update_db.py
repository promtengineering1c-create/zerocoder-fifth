import os
import sys
from sqlalchemy import select

from flask_migrate import (
    init as db_init,
    migrate as db_generate_migration,
    upgrade as db_upgrade,
)

from app import create_app
from app.models import User
from app.extensions import db

app = create_app()

def setup_database():
    with app.app_context():
        try:
            if not os.path.exists('migrations'):
                print('Инициализация окружения миграций...')
                db_init()

                print('Генерация миграций...')
                db_generate_migration(message="Initial migration")
            else:
                print('Миграции уже инициализированы.')  

            print('Применение миграций...')
            db_upgrade()
            print('Миграции применены.')

        except Exception as e:
            print(f"Критическая ошибка при работе с миграциями: {e}")
            print('Остановка работы приложения. База данных может быть в некорректном состоянии.')
            sys.exit(1)

def create_admin_user():
    with app.app_context():
        admin_username = app.config.get('ADMIN_USERNAME', 'admin')
        admin_password = app.config.get('ADMIN_PASSWORD', 'adminadmin')

        stmt = select(User).filter_by(username=admin_username)
        admin = db.session.execute(stmt).scalar_one_or_none()
        if admin:
            print(f"Пользователь {admin_username} уже существует.")
            return
        
        try:
            admin = User(username=admin_username)
            admin.set_password(admin_password)
            db.session.add(admin)

            db.session.commit()
            print(f"Администратор {admin_username} успешно создан.")
        except Exception as e:
            db.session.rollback()
            print(f"Ошибка при создании администратора: {e}")

if __name__ == '__main__':
    print("Создание базы данных...")

    setup_database()

    create_admin_user()

    print ("База данных успешно создана и настроена.")
              
                
