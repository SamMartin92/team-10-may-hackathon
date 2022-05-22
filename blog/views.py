""" Imports required by blog app """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils.text import slugify
from django.contrib import messages
from .models import Post, Comments
from .forms import BlogForm, CommentForm


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
    get_post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        # If post method update post
        form = BlogForm(request.POST, instance=get_post)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, (
                'Failed to update post. '
                'Please ensure the form is valid.'))
            return redirect(reverse(
                'edit_blog', kwargs={'post_id': post_id}))

        messages.success(request, 'Thats updated!')
        return redirect(reverse('blog'))

    else:
        # If not post method render template with prefilled form
        form = BlogForm(instance=get_post)

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': get_post,
    }

    return render(request, template, context)


def delete_blog(request, post_id):
    """ Delete blog functionality """
    del_blog = get_object_or_404(Post, pk=post_id)
    del_blog.delete()
    messages.success(request, 'Blog deleted!')
    return redirect(reverse('blog'))


def add_comment(request, post_id):
    """ Add comment to blog functionality """
    if request.method == 'POST':
        # If post method check if post doesn't already exist
        # and then add if it doesn't
        form = CommentForm(request.POST)
        if form.is_valid():
            post = get_object_or_404(Post, pk=post_id)
            instance = form.save(commit=False)
            instance.post = post
            instance.author = request.user
            instance.save()
            messages.success(request, 'Successfully added comment!')
            return redirect(reverse('blog'))
        else:
            # If form not valid return error
            messages.error(
                request, (
                    'Failed to add comment. '
                    'Please ensure the form is valid.'))
            return redirect(reverse('add_comment'))
    else:
        # If not post method render template
        form = CommentForm()
    
    template = 'blog/add_comment.html'
    get_post = get_object_or_404(Post, pk=post_id)
    context = {
        'form': form,
        'post': get_post
    }
    return render(request, template, context)
