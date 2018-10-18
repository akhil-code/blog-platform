import json

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, default=None, null=True, related_name="author")

    def __str__(self):
        return f"{self.user.first_name}"


class Tag(models.Model):
    name = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f"{self.name}"

class Blog(models.Model):
    title = models.CharField(max_length=255, blank=False)
    body = models.TextField(blank=False)
    overview = models.CharField(max_length=255, blank=True, default=None)
    contentOrder = models.CharField(max_length=255, blank=True, default=None)
    no_of_images = models.IntegerField(default=0, blank=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True, blank=False)
    tags = models.ManyToManyField(Tag, blank=True, related_name='blogs')

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def save(self, *args, **kwargs):
        contentItems = json.loads(self.body)
        s = contentItems[0]
        self.overview = s[:100]
        super(Blog, self).save(*args, **kwargs)


class Comment(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=False)
    comment = models.TextField(blank=False)
    date_posted = models.DateTimeField(auto_now_add=True, blank=False)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Comment by {self.author} on {self.blog}"

class Improvement(models.Model):
    content = models.CharField(max_length=255, blank=False)
