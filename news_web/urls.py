from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('create', views.create, name='create'),
    path('register', views.register, name='register'),
    # path('<int:post_id>', views.post_detail),
    # path('<int:post_id>/upvote', views.upvote_post)
]