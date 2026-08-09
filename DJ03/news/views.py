from django.shortcuts import get_object_or_404, redirect, render

from .models import Article
from .forms import ArticleForm

def index(request):
    return render(request, 'core/home.html')

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

def create_article(request):
    if request.method == 'POST':
        # ПЕРЕДАЕМ request.user в форму при сохранении
        form = ArticleForm(request.POST, user=request.user)
        
        if form.is_valid():
            article = form.save(commit=False)
            
            if request.user.is_authenticated:
                article.author_link = request.user
                article.author_name = request.user.username 
                
            article.save()
            
            return redirect('news:Home')
            
    else:
        # ПЕРЕДАЕМ request.user в форму при первоначальной отрисовке страницы
        form = ArticleForm(user=request.user)

    context = {
        'form': form,
        'title': 'Добавить новость',
    }
    return render(request, 'news/create.html', context)