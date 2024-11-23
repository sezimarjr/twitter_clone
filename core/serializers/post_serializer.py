from rest_framework import serializers
from core.models import Post
from django.contrib.auth.models import User

from core.models import Like


class PostSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_at', 'like_count']
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        user = self.context['request'].user
        post = Post.objects.create(user=user, **validated_data)
        return post

    def get_like_count(self, obj):
        return Like.objects.filter(post=obj).count()
