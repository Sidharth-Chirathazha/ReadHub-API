from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import CustomUser

class AuthViewTest(APITestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")

    def test_register_user(self):
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "StrongPass123",
            "confirm_password": "StrongPass123"
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["message"], "User registered successfully")

    def test_login_user(self):
        CustomUser.objects.create_user(username="tester", email="tester@example.com", password="Tester123")
        data = {"username": "tester", "password": "Tester123"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
