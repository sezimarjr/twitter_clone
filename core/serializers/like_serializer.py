from rest_framework import serializers
from core.models import Like
from django.contrib.auth.models import User


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'user', 'post']
        read_only_fields = ['id']
