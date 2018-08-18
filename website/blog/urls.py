from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('write-blog', views.blog_input_view, name='blog_input'),
    path('blog/<int:blog_id>', views.blog_view, name='blog_view'),
    path('author/<int:author_id>', views.author_posts_view, name='author_posts'),
    path('add-comment/<int:blog_id>', views.add_comment, name="add_comment"),
    path('manage', views.manage_posts_view, name='manage'),
]