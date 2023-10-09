from django.urls import path

from . import views

app_name = 'homepage'

urlpatterns = [
    # Напишите адрес тут
    path('', views.homepage, name='homepage')
    ]