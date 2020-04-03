from django.shortcuts import render
from posts.models import Post
from scrapings.models import CitizenModel


def home(request):
    context = {
        'title': 'citizen should be the title'
    }
    return render(request, 'base.html', context)


def citizen(request):
    cleaned_posts = []
    posts = CitizenModel.objects.filter('-id')[:20]
    context = {
        'title': 'citizen',
        'posts': posts,
        'something': 'another thing all together'
    }
    return render(request, 'citizen/index.html', context)


def ntv(request):
    context = {
        'title': 'ntv'
    }
    return render(request, 'ntv/index.html', context)


def ktn_news(request):
    context = {
        'title': 'ktn news'
    }
    return render(request, 'ktn_news/index.html', context)


def k24(request):
    context = {
        'title': 'k24'
    }
    return render(request, 'k24/index.html', context)
