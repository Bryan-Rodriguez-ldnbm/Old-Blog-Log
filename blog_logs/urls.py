"""Define a URL patterns for leanring_logs."""

from django.urls import path

from . import views

app_name = 'blog_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all the blogs
    path('blogs/', views.topics, name='topics')
]