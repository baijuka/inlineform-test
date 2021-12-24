from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.getName, name='getname'),
     path('thanks/', views.thanks, name='thanks' ),
]