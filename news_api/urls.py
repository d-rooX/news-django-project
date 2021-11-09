from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.posts_list),
    path("<int:pk>", views.post_detail),
    path("<int:pk>/upvote", views.post_upvote),
    path("<int:pl>/comment", views.create_comment),
]

urlpatterns = format_suffix_patterns(urlpatterns)
