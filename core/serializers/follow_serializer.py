from rest_framework import serializers
from core.models import Follow
from django.contrib.auth.models import User


class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.StringRelatedField()
    followed = serializers.StringRelatedField()

    class Meta:
        model = Follow
        fields = ['id', 'follower', 'followed']
        read_only_fields = ['id']
