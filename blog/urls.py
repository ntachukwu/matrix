from django.urls import path
from .views import PostList, post_detail

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>/', post_detail, name="post_detail"),
]
