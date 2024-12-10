from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
                username="test", 
                email="test@test.ts",
                password="testpass1234"
                )
        self.assertEqual(user.username, "test")
        self.assertEqual(user.email, "test@test.ts")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
                username="test",
                email="admin@admin.ts",
                password="testpass1234"
                )
        self.assertEqual(user.username, "test")
        self.assertEqual(user.email, "admin@admin.ts")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

