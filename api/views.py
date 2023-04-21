from django.shortcuts import get_object_or_404
from rest_framework import generics, status, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView
from insta_app.models import Post
from api.serializer import PostSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, user=self.request.user)


class PostLikeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.likes.add(request.user)
        return Response({'status': 'success'})

    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.likes.remove(request.user)
        return Response({'status': 'success'})


class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            raise PermissionDenied
        return self.update(request, *args, **kwargs)


class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            raise PermissionDenied
        return super().delete(request, *args, **kwargs)
