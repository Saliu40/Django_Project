#we create this file manually on the project
#we added everything here
from django.urls import path
from . import views
 
urlpatterns = [
    path('index/', views.index, name='blog-index'),
    path('about/', views.about, name='blog-about'),
    path('news/', views.news, name='blog-news'),
]
 