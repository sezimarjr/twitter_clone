from rest_framework.generics import RetrieveAPIView
from core.models import Profile
from core.serializers import ProfileSerializer
from django.shortcuts import get_object_or_404


class ProfileByUsernameView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        username = self.kwargs['username']
        return get_object_or_404(Profile, user__username=username)
