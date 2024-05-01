from django.urls import path
from. import views

urlpatterns = [
    path('register/', views.register, name='forms-register'),
    path('success/', views.success, name='forms-success'),
]