from django.urls import include, path
from rest_framework import routers

from users import views as user_views

router = routers.DefaultRouter()

router.register(r"users", viewset=user_views.UserViewSet, basename="user")
