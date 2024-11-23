from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import Profile  # Seu modelo Profile


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # Não inclui o profile aqui

    def create(self, validated_data):
        # Criação do usuário
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        # Criação do Profile associado ao usuário
        # Cria um profile vazio para o usuário
        Profile.objects.create(user=user)

        return user
