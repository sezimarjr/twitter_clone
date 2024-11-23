from rest_framework import serializers
from core.models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ['id, user, content, created_at']
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
