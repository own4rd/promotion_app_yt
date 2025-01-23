from django.shortcuts import render
from promotions.models.post import Post

def home_view(request):
    posts = Post.objects.all().prefetch_related('tags').select_related('category')
    context = {
        'promotions': posts
    }
    return render(request, 'home/index.html', context)
