from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_auth.serializers import JWTSerializer
from django.conf import settings

User = get_user_model()


class EmailTokenObtainSerializer(TokenObtainSerializer):
    username_field = User.EMAIL_FIELD


class CustomTokenObtainPairSerializer(EmailTokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        # token = super().get_token(user)
        # token["name"] = user.name
        # return token
        # return AccessToken.for_user(user)
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data


# class CustomJWTSerializer(JWTSerializer):
#     user = serializers.SerializerMethodField()
#     token = CustomTokenObtainPairSerializer.get_token(user)

#     def get_user(self, obj):
#         user_data = obj["user"], context=self.context
#         return user_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email")

