# core/models.py
from django.db import models

class TimeStampedModel(models.Model):
    """
    Абстрактная модель, которая добавляет дату создания
    и дату изменения ко всем наследующим её моделям.
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")

    class Meta:
        abstract = True