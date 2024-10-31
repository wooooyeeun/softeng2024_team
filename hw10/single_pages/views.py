

from django.shortcuts import render
import pandas as pd

# Create your views here.
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
    return render(request, 'single_pages/blog.html', {'title': "blog", 'posts': post_list})

def portfolio_page(request):
    return render(request, 'single_pages/portfolio.html', {'title': 'Portfolio'})
