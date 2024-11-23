from rest_framework.viewsets import ModelViewSet
from core.models import Post
from core.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()  # Define que vamos retornar todos os posts
    serializer_class = PostSerializer  # Indica qual serializer usar para os dados
    permission_classes = [
        IsAuthenticated
    ]
