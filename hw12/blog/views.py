from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 5

class PostDetail(DetailView):
    model = Post

