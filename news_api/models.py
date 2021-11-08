from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(get_user_model(), models.SET_NULL, null=True)
    upvotes = models.IntegerField(default=0)
    link = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), models.SET_NULL, null=True)
    post = models.ForeignKey(Post, models.CASCADE)
    text = models.TextField()
