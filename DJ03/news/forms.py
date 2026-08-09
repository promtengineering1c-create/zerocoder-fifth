from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'content', 'pub_date']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'author_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя или псевдоним'}),
        }

    def __init__(self, *args, **kwargs):
        # Аккуратно вытаскиваем (берем и удаляем) пользователя из именованных аргументов.
        # Если его там нет, возвращаем None (чтобы код не упал с ошибкой).
        user = kwargs.pop('user', None)
        
        # Вызываем оригинальный __init__ родительского класса, чтобы форма собралась как обычно
        super().__init__(*args, **kwargs)

        if user and user.is_authenticated:
            self.fields.pop('author_name', None)