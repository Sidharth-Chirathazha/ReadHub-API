from django.test import TestCase
from users.serializers import RegistrationSerializer
from users.models import CustomUser

class RegistrationSerializerTest(TestCase):
    def test_valid_data_creates_user(self):
        data = {
            "username": "user1",
            "email": "user1@example.com",
            "password": "Password@123",
            "confirm_password": "Password@123"
        }
        serializer = RegistrationSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        user = serializer.save()
        self.assertEqual(user.username, "user1")
        self.assertEqual(user.email, "user1@example.com")
        self.assertTrue(user.check_password("Password@123"))

    def test_password_mismatch(self):
        data = {
            "username": "user2",
            "email": "user2@example.com",
            "password": "Password@123",
            "confirm_password": "Mismatch@123"
        }
        serializer = RegistrationSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("non_field_errors", serializer.errors)

