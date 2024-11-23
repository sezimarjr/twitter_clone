from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Profile


from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Profile


from rest_framework import serializers
from core.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Mostrar o username

    class Meta:
        model = Profile
        # Inclua os campos que você deseja exibir
        fields = ['id', 'user', 'bio', 'location', 'birth_date']
        read_only_fields = ['id', 'user', 'bio', 'location',
                            'birth_date']  # Torna tudo somente leitura
