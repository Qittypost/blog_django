from django.shortcuts import render
from .models import Post, Author


def get_posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'blog/post_list.html', context)


def post_details(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post,
        'published_recently': post.published_recently()
    }

    return render(request, 'blog/post_detail.html', context)


def author_posts(request, pk):
    author = Author.objects.get(id=pk)
    context = {
        'posts': author.post.all()
    }

    return render(request, 'blog/post_list.html', context)
