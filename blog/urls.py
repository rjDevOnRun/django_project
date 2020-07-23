from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # format: name, view.method name, name
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]