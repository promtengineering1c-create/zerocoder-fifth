from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='Home'),
    path('page2/', views.page_2, name='Page2'),
    path('page3/', views.page_3, name='Page3'),
]