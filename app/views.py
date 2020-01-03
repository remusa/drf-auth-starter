from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


CustomUser = get_user_model()


@api_view(["GET"])
def api_root(request, format=None):
    return Response({"users": reverse("user-list", request=request, format=format),})
