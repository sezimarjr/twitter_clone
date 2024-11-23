from rest_framework import serializers
from core.models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(
        source='user.id', read_only=True)  # ID do usuário
    username = serializers.CharField(
        source='user.username', read_only=True)  # Nome do usuário
    email = serializers.EmailField(
        source='user.email', read_only=True)  # Email do usuário

    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'bio',
                  'location', 'birth_date', 'avatar']
