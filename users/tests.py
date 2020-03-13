from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        test_email = "testuser@test.com"
        test_username = "testuser"
        test_password = "testuser123"

        User = get_user_model()
        user = User.objects.create_user(
            email=test_email, username=test_username, password=test_password
        )

        self.assertEqual(user.email, test_email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin_email = "admin@admin.com"
        admin_username = "admin"
        admin_password = "admin123456"

        User = get_user_model()
        user = User.objects.create_superuser(
            email=admin_email, username=admin_username, password=admin_password
        )

        self.assertEqual(user.email, admin_email)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
