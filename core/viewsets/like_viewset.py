from rest_framework.viewsets import ModelViewSet
from core.models import Like

from core.serializers import LikeSerializer


from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
