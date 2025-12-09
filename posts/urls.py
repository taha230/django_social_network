from django.contrib import admin
from django.urls import path
from .views import PostView, PostListView



urlpatterns = [
    path('post/', PostView.as_view(), name='post'),
    path('post/<int:post_pk>/', PostView.as_view(), name='post'),
    path('posts-list/', PostListView.as_view(), name='posts-list'),

]
