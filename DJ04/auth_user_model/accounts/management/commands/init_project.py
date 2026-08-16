import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

# Хорошая практика: всегда получаем текущую модель пользователя динамически,
# чтобы код не сломался, если мы решим переименовать класс core.User
User = get_user_model()

class Command(BaseCommand):
    # help выводится, когда кто-то пишет python manage.py help
    help = 'Первичная инициализация проекта: создание суперпользователя и базовых настроек'

    def handle(self, *args, **kwargs):
        # 1. Читаем доступы из окружения. Если их нет — берем дефолтные (удобно для локалки)
        admin_username = settings.SUPERUSER_USERNAME
        admin_password = settings.SUPERUSER_PASSWORD
        admin_email = settings.SUPERUSER_EMAIL

        # 2. Идемпотентность: проверяем, нет ли уже такого пользователя
        if User.objects.filter(username=admin_username).exists():
            self.stdout.write(self.style.WARNING(f'Суперпользователь "{admin_username}" уже существует. Пропускаем.'))
        else:
            # 3. Создаем суперпользователя через ORM
            User.objects.create_superuser(
                username=admin_username,
                email=admin_email,
                password=admin_password
            )
            self.stdout.write(self.style.SUCCESS(f'Суперпользователь "{admin_username}" успешно создан!'))
            
        # Здесь же в будущем можно добавить создание дефолтных категорий, ролей и т.д.