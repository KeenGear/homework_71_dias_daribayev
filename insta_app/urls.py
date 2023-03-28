from django.urls import path
from .views import PostListView, PostCreateView, like_post, unlike_post, PostUpdateView, PostDeleteView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('post_delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('post_update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/unlike/', unlike_post, name='unlike_post'),
    path('post/<int:pk>/like/', like_post, name='like_post'),
]
