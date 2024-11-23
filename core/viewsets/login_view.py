from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.data)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Inicia a sessão
            return JsonResponse({'detail': 'Login bem-sucedido'})
        return JsonResponse({'detail': 'Credenciais inválidas'}, status=400)
