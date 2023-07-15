from django.shortcuts import render, redirect

from .models import Post

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'blog_logs/index.html')

def posts(request):
    """Show all Bogs and its associated Entry"""
    posts = Post.objects.order_by('-date_added')
    paginator = Paginator(posts, 4)
    page_num = request.GET.get('page')

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    context = {'page_obj': page_obj}

    return render(request, 'blog_logs/posts.html', context)

def post(request, post_id):
    """Show the full post"""
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blog_logs/post.html', context)
