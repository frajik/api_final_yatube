from rest_framework import serializers

from rest_framework.validators import UniqueTogetherValidator
from posts.models import Comment, Post, Follow, Group
from django.contrib.auth import get_user_model

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        fields = ("id", "text", "pub_date", "author", "image", "group",)
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ("id", "author", "post", "text", "created",)
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("id", "title", "slug", "description",)
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all(),
    )
    user = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        fields = ("following", "user",)
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(), fields=("following", "user")
            )
        ]

    def validate(self, data):
        if self.context["request"].user == data["following"]:
            raise serializers.ValidationError("Нельзя подписаться на себя.")
        return data
