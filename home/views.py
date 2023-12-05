from django.shortcuts import render
from .models import Post,Category,Tag

def home(request):
    popular_post=Post.objects.filter(section='Popular').order_by('-id')[0:4]
    recent_post=Post.objects.filter(section='Recent').order_by('-id')[:4]
    main_post=Post.objects.filter(mainpost=True)[:1]
    editors_pick=Post.objects.filter(section='Editors_Pick').order_by('-id')
    trending= Post.objects.filter(section = 'Trending').order_by('-id')
    inspiration=Post.objects.filter(section='Inspiration').order_by('-id')[:3]
    latest_post=Post.objects.filter(section='Latest_Posts').order_by('-id')[:4]
    category=Category.objects.all()
    tags = Tag.objects.values('name').distinct()[:5]

    
    context={
        'popular_post':popular_post,
        'recent_post':recent_post,
        'main_post':main_post,
        'editors_pick':editors_pick,
        'trending':trending,
        'inspiration':inspiration,
        'latest_post':latest_post,
        'category':category,
        'tags':tags,
    }

    return render(request,'index.html',context)
