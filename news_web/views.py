from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
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
            return redirect('index')

        errors = form.errors

    form = PostInput()
    return render(request, 'news_web/create.html', {'form': form, 'errors': errors})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def index(request):
    posts = Post.objects.all()
    data = {
        'posts': posts,
    }
    return render(request, 'news_web/index.html', data)

