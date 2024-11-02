from django.shortcuts import render
from .models import Post
import pandas as pd

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post
        }
    )

def landing_page(request):
    return render(request, 'single_pages/landing.html', {'title': 'Home'})

def about_page(request):
    return render(request, 'single_pages/about.html', {'title': 'About'})

def blog_list(request):
    df = pd.read_csv("data.csv")
    post_list = []
    for i, row in df.iterrows():
        post_list.append({
            "title": row['title'],
            "content": row['content']})
    return render(request, 'single_pages/blog_page.html', {'title': "Blog", 'posts': post_list})

def portfolio_page(request):
    return render(request, 'single_pages/portfolio.html', {'title': 'Portfolio'})

