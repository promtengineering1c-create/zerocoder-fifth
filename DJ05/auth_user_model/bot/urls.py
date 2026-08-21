from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('user/<int:user_id>/', views.get_user, name='get_user'),
]