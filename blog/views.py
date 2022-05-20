""" Imports required by blog app """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Post, Comments


def blog_posts(request):
    """ Get blog posts """
    all_posts = Post.objects.all()
    context = {
        'posts': all_posts,
    }
    return render(request, 'blog/blog.html', context)


def post_details(request, slug):
    """ Get blog details """
    post = get_object_or_404(Post, slug=slug)
    comments = Comments.objects.filter(post=post.pk)
    context = {
        'post': post,
        'comments': comments,
    }

    return render(request, 'blog/post_detail.html', context)


def add_post(request):

    return render(request, 'blog/add_post.html')


def edit_blog(request, post_id):
    """ Edit post """
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
    }

    return render(request, 'blog/edit_post.html', context)


def delete_blog(request, post_id):
    """ Delete blog functionality """
    del_blog = get_object_or_404(Post, pk=post_id)
    del_blog.delete()
    messages.success(request, 'Blog deleted!')
    return redirect(reverse('blog'))


def add_comment(request, post_id):
    """ Add comment to blog functionality """

    return render(request, "blog/add_comment.html")
