from django.contrib import admin
from django.urls import path
from . import views  # "." means call subject in the same directory

app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name='register'),
]
