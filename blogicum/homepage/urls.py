from django.urls import path

from . import views

app_name = 'homepage'
# Напишите адрес тут
urlpatterns = [path('', views.homepage, name='homepage')]
