from rest_framework.generics import RetrieveAPIView
from core.models import Profile
from core.serializers import ProfileSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication


class ProfileByUsernameView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [SessionAuthentication]  # Autenticação via sessão
    # Apenas usuários autenticados podem acessar
    permission_classes = [IsAuthenticated]

    def get_object(self):
        username = self.kwargs['username']
        return get_object_or_404(Profile, user__username=username)
