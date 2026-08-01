from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('data/', views.data, name='data'),
    path('test/', views.test, name='test'),
]