from django.contrib.auth import get_user_model
from rest_framework import serializers

CustomUser = get_user_model()

# HyperlinkedModelSerializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user-detail")

    class Meta:
        model = CustomUser
        fields = (
            "url",
            "id",
            "username",
            "email",
        )

