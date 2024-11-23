from django.urls import path, include
from rest_framework import routers

from core import viewsets

router = routers.DefaultRouter()
router.register(r'posts', viewsets.PostViewSet)
router.register(r'profiles', viewsets.ProfileViewSet)
router.register(r'follows', viewsets.FollowViewSet)
router.register(r'likes', viewsets.LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]