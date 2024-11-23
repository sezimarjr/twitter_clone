from rest_framework import serializers
from core.models import Like
from django.contrib.auth.models import User

from core.models import Post


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Like
        fields = ['id', 'user', 'post']
        read_only_fields = ['id']
