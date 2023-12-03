from django.shortcuts import render
from .models import Post

def home(request):
    popular_post=Post.objects.filter(section='Popular').order_by('-id')[0:4]
    recent_post=Post.objects.filter(section='Recent').order_by('-id')
    context={
        'popular_post':popular_post,
        'recent_post':recent_post
    }

    return render(request,'index.html',context)
