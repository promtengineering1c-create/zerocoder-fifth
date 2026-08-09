from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='Home'),
    path('page2/', views.page_2, name='Page2'),
    path('<int:article_id>/', views.detail, name='detail'),
]