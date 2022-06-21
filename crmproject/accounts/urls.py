from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home), # empty string is the base URL
    path('products/', views.products), 
    path('customer/<str:pk_customer>/', views.customer),
]