from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
   post = Post.objects.all().order_by('-pk')

   return render(
       request,
       'blog/index.html',
       {
           'posts': post
       }
   )

def single_post(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post.html',
        {
            'post': post,
        }
    )