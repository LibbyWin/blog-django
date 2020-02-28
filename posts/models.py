from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
    A single Blog post
    Blog needs a title/content/dates/how many views/whos tagged/images
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)"""as soon as the thing is created it will add that date and time"""
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)"""will be the current time published"""
    views = models.IntegerField(default=0)"""number field, starts off at 0 views"""
    tag = models.CharField(max_length=30, blank=True, null=True)"""add tags for filtering needs"""
    image = models.ImageField(upload_to="img", blank=True, null=True)"""allows users to upload images/ will upload to media/img directory."""

    def __unicode__(self):
        return self.title