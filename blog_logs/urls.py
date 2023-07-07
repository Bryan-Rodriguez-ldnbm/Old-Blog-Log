"""Define a URL patterns for blog_logs."""

from django.urls import path

from . import views

app_name = 'blog_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all the posts
    path('posts/', views.posts, name='posts'),
    # Detail page for a single post
    path('posts/<int:post_id>', views.post, name='post'),
]
