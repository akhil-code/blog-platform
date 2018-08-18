from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, default=None, null=True, related_name="author")
    posts = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    rating = models.DecimalField(default=0.0, decimal_places=6, max_digits=7)

    def __str__(self):
        return f"{self.user.first_name}"


class Tag(models.Model):
    name = models.CharField(max_length=255, blank=True)
    views = models.IntegerField(default=0)
    posts = models.IntegerField(default=0)
    rating = models.DecimalField(default=0.0, decimal_places=6, max_digits=7)
    
    def __str__(self):
        return f"{self.name}"

class Blog(models.Model):
    title = models.CharField(max_length=255, blank=False)
    body = models.TextField(blank=False)
    contentOrder = models.CharField(max_length=255, blank=True, default=None)
    no_of_images = models.IntegerField(default=0, blank=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True, blank=False)
    tags = models.ManyToManyField(Tag, blank=True, related_name='blogs')

    def __str__(self):
        return f"{self.title} by {self.author}"


class Comment(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=False)
    comment = models.TextField(blank=False)
    date_posted = models.DateTimeField(auto_now_add=True, blank=False)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Comment by {self.author} on {self.blog}"

class Website(models.Model):
    tag_views = models.IntegerField(default=0)
    author_views = models.IntegerField(default=0)
    posts = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    def __str__(self):
        return f"website stats(Don't touch)"