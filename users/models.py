import uuid

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models import Q


class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        return self.get(
            Q(**{self.model.USERNAME_FIELD: username}) | Q(**{self.model.EMAIL_FIELD: username})
        )


class CustomUser(AbstractUser):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        verbose_name="username", max_length=255, unique=True, null=True, blank=True
    )
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
