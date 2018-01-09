from django.urls import path
from visible import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('article', views.article, name='article'),
]