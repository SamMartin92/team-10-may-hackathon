""" Imports required for blog app urls """
from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_posts, name='blog'),
    path('create_post/', views.create_post, name='create_post'),
    path('<slug:slug>/', views.post_details, name='post_detail'),
    path('edit_blog/<int:post_id>/', views.edit_blog, name='edit_blog'),
    path('delete_blog/<int:post_id>/', views.delete_blog, name='delete_blog'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
]
