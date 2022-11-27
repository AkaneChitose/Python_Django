from django.contrib import admin
from django.urls import path
from . import views  # "." means call subject in the same directory

urlpatterns = [
    path('', views.index),
    path('products/', views.products),
    # path('main/', views.index)
]
