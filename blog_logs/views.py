from django.shortcuts import render

from .models import BlogTopic

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'blog_logs/index.html')

def BlogTopic(request, topic_id):
    """Show a single Blog and its associated Entry"""
    blog = BlogTopic.object.get(id=topic_id)
    entries = blog.entry_set.order_by('-date_added')
    context = {'blog': blog, 'entries': entries}
    return render(request, 'blog_logs/index.html')