from django.test import TestCase
from users.models import CustomUser

class CustomUserModelTest(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("testpass123"))
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        admin = CustomUser.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpass123"
        ) 
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
