from django.urls import path
from .views import PostList, PostDetail, PostListCreateAPIView, PostLikeAPIView, PostUpdateAPIView, PostDeleteAPIView

app_name = 'insta_app_api'

urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('posts/<int:pk>/update/', PostUpdateAPIView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteAPIView.as_view(), name='post_delete'),
    path('create-post/', PostListCreateAPIView.as_view(), name='post_create'),
    path('like-post/<int:pk>/', PostLikeAPIView.as_view(), name='post_like'),
]
