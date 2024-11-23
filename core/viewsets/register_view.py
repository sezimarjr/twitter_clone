from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from core.serializers import RegisterSerializer


class RegisterUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Cria o usuário e o profile
            return Response({
                "message": "Usuário criado com sucesso",
                "user": {
                    "username": user.username,
                    "email": user.email
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
