from rest_framework import viewsets
from core.models import Profile
from core.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()  # Todos os perfis
    serializer_class = ProfileSerializer  # O serializer que será usado
