from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='Home'),
    path('data/', views.data, name='Data'),
    path('test/', views.test, name='Test'),
    path('page2/', views.page_2, name='Page2'),
    path('page3/', views.page_3, name='Page3'),
    path('page4/', views.page_4, name='Page4'),
]