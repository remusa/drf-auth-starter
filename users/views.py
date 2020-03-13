from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer

CustomUser = get_user_model()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated, IsAdminUser]
    permission_classes = [IsAdminUser]
    pagination_classes = [PageNumberPagination]
