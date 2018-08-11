from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/<int:blog_id>', views.blog_view, name='blog_view'),
    path('blogs/<int:author_id>', views.author_posts_view, name='author_posts'),
]