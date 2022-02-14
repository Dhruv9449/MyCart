from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='BlogHome'),
    path('blogpost/<int:bid>', views.blogPost, name='BlogPost')
]
