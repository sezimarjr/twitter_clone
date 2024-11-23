from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Profile


from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # Campos que o usuário pode atualizar no perfil
        fields = ['bio', 'birth_date', 'avatar']


class UserSerializer(serializers.ModelSerializer):
    # Não exigimos o perfil na criação
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        # Excluímos o perfil de ser obrigatório
        fields = ['username', 'email', 'password', 'profile']

    def create(self, validated_data):
        # Não espera dados do perfil na criação
        profile_data = validated_data.pop('profile', None)

        # Cria o usuário com dados fornecidos
        user = User.objects.create_user(**validated_data)

        # Criação do perfil vazio (sem dados) após criar o usuário
        Profile.objects.create(user=user)

        return user
