from django.shortcuts import render
from .models.post import Post


def detail_promotion(request, slug):
    promotion = Post.objects.get(slug=slug)
    return render(request, 'promotions/detail_promotion.html', {'promotion': promotion})    

