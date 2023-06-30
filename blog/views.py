from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Post


def hello_world_view(request):
    return redirect('/posts/')


def posts_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, 'index.html', {'posts': posts})


def posts_detail_view(request, id):
    if request.method == "GET":
        post = Post.objects.get(id=id)
        return render(request, 'post_detail.html', {'post': post})


def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Пост успешно добавлен')
    else:
        form = PostForm
    return render(request, 'create_post.html', {'form': form})


def post_update_view(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Пост успешно обновлен</h2>')
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post
    }
    return render(request, 'update_post.html', context)


def post_delete_view(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponse('Пост удален из Базы данных')
