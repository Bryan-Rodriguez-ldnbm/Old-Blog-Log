"""Define a URL patterns for leanring_logs."""

from django.urls import path

from . import views

app_name = 'blog_logs'
urlpatters = [
    # Home page
    path('', views.index, name='index'),
]