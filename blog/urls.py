""" Imports required for blog app urls """
from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_posts, name='blog'),
]
