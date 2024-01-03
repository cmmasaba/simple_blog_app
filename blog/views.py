from django.views.generic import ListView, DetailView

from .models import Post


class BlogListView(ListView):
    """class view for the blog page"""
    model = Post
    template_name = 'home.html'
