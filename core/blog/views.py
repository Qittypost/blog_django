from django.shortcuts import render
from .models import Post


def get_posts(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})
