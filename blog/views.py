""" Imports required by blog app """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils.text import slugify
from django.contrib import messages
from .models import Post, Comments
from .forms import BlogForm


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


def create_post(request):
    """ Add post view """
    if request.method == 'POST':
        # If post method check if post doesn't already exist
        # and then add if it doesn't
        form = BlogForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            try:
                Post.objects.get(
                    title__iexact=form.cleaned_data.get("title"))
                messages.error(request, (
                    'Blog name taken.'))
                return redirect(reverse('add_post'))

            except Post.DoesNotExist:
                instance.author = request.user
                instance.status = 1
                instance.slug = slugify(instance.title)
                instance.save()
                messages.success(request, 'Successfully added post!')
                return redirect(reverse('blog'))
        else:
            # If form not valid return error
            messages.error(
                request, (
                    'Failed to add post. '
                    'Please ensure the form is valid.'))
            return redirect(reverse('add_post'))
    else:
        # If not post method render template
        form = BlogForm()

    template = 'blog/create_post.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


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
