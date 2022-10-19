from posts.models import Post, Group, Follow
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer
)
from rest_framework import viewsets, filters, permissions
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        new_queryset = get_object_or_404(Post, pk=post_id)
        return new_queryset.comments.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("following__username",)
    http_method_names = ["get", "post"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.request.user.follower.all()
