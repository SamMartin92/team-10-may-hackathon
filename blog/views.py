""" Imports required by blog app """
from django.shortcuts import render
from .models import Post, Comments


def blog_posts(request):
    """ Get blog posts """
    all_posts = Post.objects.all()
    all_comments = Comments.objects.all()
    context = {
        'posts': all_posts,
        'comments': all_comments,
    }

    return render(request, 'blog/blog.html', context)
