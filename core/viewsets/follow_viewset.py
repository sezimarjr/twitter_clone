from rest_framework import viewsets
from core.models import Follow
from core.serializers import FollowSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()  # Todos os relacionamentos de follow
    serializer_class = FollowSerializer  # O serializer para o follow
