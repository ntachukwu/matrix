from django.urls import path
from django.conf.urls import url
from .views import PostList, post_detail, like_post

urlpatterns = [
    path('<slug:slug>/', post_detail, name="post_detailing"),
    path('', PostList.as_view(), name='home'),
    path('like/<slug:slug>/', like_post, name='like'),


]
