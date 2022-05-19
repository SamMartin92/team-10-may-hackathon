""" Imports for blog app models"""
from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    """ Creates blog table in database"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """ Displays posts, newest first """
        ordering = ['-created_on']

    def __str__(self):
        """ Override default str method """
        return self.title


class Comments(models.Model):
    """ Creates comments table in database"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Displays comments, newest first """
        ordering = ['-created_on']

    def __str__(self):
        """ Override default str method """
        return self.content
