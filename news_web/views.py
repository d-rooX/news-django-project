from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from news_api.models import Post
from .forms import PostInput


@login_required
def create(request):
    errors = ''
    if request.method == 'POST':
        form = PostInput(request.POST)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('/')

        errors = form.errors

    form = PostInput()
    return render(request, 'news_web/create.html', {'form': form, 'errors': errors})


def index(request):
    posts = Post.objects.all()
    data = {
        'posts': posts,
    }
    return render(request, 'news_web/index.html', data)

