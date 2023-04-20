from django.urls import path
from .views import PostList, PostDetail, PostListCreateAPIView, PostLikeAPIView

app_name = 'insta_app_api'

urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('create-post/', PostListCreateAPIView.as_view(), name='post_create'),
    path('like-post/<int:pk>/', PostLikeAPIView.as_view(), name='post_like'),
]
