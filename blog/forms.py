""" Imports required for forms """
from django import forms
from .models import Post


class BlogForm(forms.ModelForm):
    """ Create BlogForm class """
    class Meta:
        """ Fields to render from model """
        model = Post
        exclude = ('author', 'slug', 'update_on', 'created_on', 'status')

    def __init__(self, *args, **kwargs):
        """ Add placeholders and required attribute,
        set autofocus on first field """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['required'] = True
        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields['content'].widget.attrs['placeholder'] = (
            "e.g Tell us how you're feeling or how your day was.")
