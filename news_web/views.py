from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from news_api.models import Post, Comment, Upvote
from .forms import PostInput, CommentInput


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


@login_required
def upvote_post(request, post_id):
    post = Post.objects.get(id=post_id)
    user_upvote = post.upvotes.filter(author_id=request.user.id)
    if user_upvote:
        user_upvote.delete()
    else:
        user_upvote = Upvote(author=request.user, post=post)
        user_upvote.save()

    post.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))


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


def post_comments(request, post_id):
    errors = ''
    if request.method == 'POST':
        form = CommentInput(request.POST)
        if form.is_valid():
            comment = Comment(**form.cleaned_data)
            comment.author = request.user
            comment.post_id = post_id
            comment.save()
        else:
            errors = form.errors.values()

    if request.user.is_authenticated:
        form = CommentInput()
    else:
        form = None

    post = Post.objects.get(id=post_id)
    comments = post.comments.all().order_by('-id')
    data = {
        'form': form,
        'post': post,
        'errors': errors,
        'comments': comments,
    }
    return render(request, 'news_web/post.html', data)
