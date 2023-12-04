from django.shortcuts import render
from .models import Post

def home(request):
    popular_post=Post.objects.filter(section='Popular').order_by('-id')[0:4]
    recent_post=Post.objects.filter(section='Recent').order_by('-id')[:4]
    main_post=Post.objects.filter(mainpost=True)[:1]
    editors_pick=Post.objects.filter(section='Editors_Pick').order_by('-id')
    trending= Post.objects.filter(section = 'Trending').order_by('-id')
    context={
        'popular_post':popular_post,
        'recent_post':recent_post,
        'main_post':main_post,
        'editors_pick':editors_pick,
        'trending':trending
    }

    return render(request,'index.html',context)
