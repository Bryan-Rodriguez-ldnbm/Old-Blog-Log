from django.shortcuts import render

from .models import Post

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'blog_logs/index.html')

def posts(request):
    """Show all Bogs and its associated Entry"""
    posts = Post.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blog_logs/posts.html', context)

def post(request, post_id):
    """Show the full post"""
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blog_logs/post.html', context)
