from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('news', views.posts_list),
    path('news/<int:pk>', views.post_detail),
    path('news/<int:pk>/upvote', views.post_upvote)
]

urlpatterns = format_suffix_patterns(urlpatterns)
