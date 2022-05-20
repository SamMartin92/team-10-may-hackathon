""" Register blog models with admin so that it appears in admin dashboard"""
from django.contrib import admin
from .models import Post, Comments


class PostAdmin(admin.ModelAdmin):
    """Change display in admin panel to see important information """
    list_display = (
        'author',
        'title',
        'slug',
        'created_on',
    )
    ordering = ('created_on',)
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    """Change display in admin panel to see important information """
    list_display = (
        'post',
        'author',
        'created_on',
    )
    ordering = ('post',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentAdmin)
