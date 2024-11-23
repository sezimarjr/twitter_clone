from rest_framework.viewsets import ModelViewSet
from core.models import Like
from core.models import Post
from core.serializers import LikeSerializer

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    # Ação para curtir o post
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = Post.objects.get(pk=pk)  # Obtém o post pelo ID
        user = request.user  # Usuário autenticado

        # Verifica se o usuário já curtiu o post
        if Like.objects.filter(post=post, user=user).exists():
            return Response({'detail': 'Você já curtiu esse post.'}, status=status.HTTP_400_BAD_REQUEST)

        # Cria um novo like
        Like.objects.create(post=post, user=user)
        return Response({'detail': 'Post curtido com sucesso!'}, status=status.HTTP_201_CREATED)

    # Ação para descurtir o post
    @action(detail=True, methods=['delete'])
    def unlike(self, request, pk=None):
        post = Post.objects.get(pk=pk)  # Obtém o post pelo ID
        user = request.user  # Usuário autenticado

        # Verifica se o usuário curtiu o post
        like = Like.objects.filter(post=post, user=user).first()
        if not like:
            return Response({'detail': 'Você ainda não curtiu esse post.'}, status=status.HTTP_400_BAD_REQUEST)

        # Remove o like
        like.delete()
        return Response({'detail': 'Like removido com sucesso!'}, status=status.HTTP_204_NO_CONTENT)
