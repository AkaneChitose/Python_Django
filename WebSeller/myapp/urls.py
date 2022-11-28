from django.contrib import admin
from django.urls import path
from . import views  # "." means call subject in the same directory

app_name = 'myapp'
urlpatterns = [
    path('', views.index),
    path('products/', views.products),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
]
