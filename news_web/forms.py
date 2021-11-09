from django import forms
from news_api.models import Post


class PostInput(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'link']
