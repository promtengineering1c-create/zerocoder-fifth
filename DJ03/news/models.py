from django.utils import timezone

from django.db import models
from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.CharField(max_length=500, blank=True, verbose_name='Описание')
    content = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    
    # 1. Системная ссылка на профиль (может быть пустой)
    author_link = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, 
        null=True,                 
        blank=True,                
        related_name='articles',
        verbose_name='Профиль автора'
    )
    
    # 2. Текстовое имя (для анонимов и для сохранения истории)
    author_name = models.CharField(
        max_length=255,
        verbose_name='Имя автора',
        help_text='Заполняется автоматически или вручную для анонимов'
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-pub_date']

    def __str__(self):
        return self.title