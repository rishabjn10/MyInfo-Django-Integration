from django.urls import reverse
from rest_framework.test import APITestCase

class MyInfoAPITests(APITestCase):
    def test_auth_login(self):
        url = reverse('auth-login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('auth_url', response.data)

    def test_auth_callback_without_code(self):
        url = reverse('auth-callback')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)
