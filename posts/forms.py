from django import forms """import formas files"""
from .models import Post


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date')