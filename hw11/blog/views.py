from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
import pandas as pd

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

def landing_page(request):
    return render(request, 'todo_app/landing.html', {'title': 'Home'})

def about_page(request):
    return render(request, 'todo_app/about.html', {'title': 'About'})

def blog_list(request):
    df = pd.read_csv("data.csv")
    post_list = []
    for i, row in df.iterrows():
        post_list.append({
            "title": row['title'],
            "content": row['content']})
    return render(request, 'todo_app/blog_page.html', {'title': "Blog", 'posts': post_list})

def portfolio_page(request):
    return render(request, 'todo_app/portfolio.html', {'title': 'Portfolio'})