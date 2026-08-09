from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # Указываем поля из модели, которые хотим видеть в таблице.
    list_display = ('title', 'author_name', 'pub_date', 'author_link')
    
    # list_filter — добавляет боковую панель с быстрыми отборами.
    list_filter = ('pub_date', 'author_link')
    
    # search_fields — добавляет строку поиска над таблицей.
    # Ищет по тексту (использует SQL-оператор LIKE).
    search_fields = ('title', 'author_name', 'content')
    
    # Делаем заголовок кликабельным для перехода в карточку редактирования
    list_display_links = ('title',)