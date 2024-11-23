from django.urls import path, include
from rest_framework import routers

from core import viewsets


router = routers.DefaultRouter()
router.register(r'posts', viewsets.PostViewSet)
router.register(r'profiles', viewsets.ProfileViewSet)
router.register(r'follows', viewsets.FollowViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', viewsets.RegisterUserView.as_view()),
    path('profile/<str:username>/',
         viewsets.ProfileByUsernameView.as_view(), name='profile_by_username')
]
