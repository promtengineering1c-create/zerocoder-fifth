from django.shortcuts import get_object_or_404, render

from .models import Article

def index(request):
    return render(request, 'core/home.html')

# Create your views here.
def page_2(request):

    news_list = Article.objects.all()
    
    context = {
        'news': news_list,
        'title': 'Главные новости', 
    }
    
    return render(request, 'news/page_2.html', context)

def detail(request, article_id):
    # Пытаемся достать статью по ID. Если не выйдет - отдаем 404
    article = get_object_or_404(Article, id=article_id)
    
    context = {
        'article': article,
        'title': article.title, # Передаем заголовок статьи в тег <title>
    }
    
    return render(request, 'news/detail.html', context)
