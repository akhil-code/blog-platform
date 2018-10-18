from django.contrib import admin

from .models import Author, Blog, Comment, Tag

# Register your models here.
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Tag)
