"""
Test User API Endpoint
"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')
ME_URL = reverse('user:me')


def create_user(**params):
    """Return created users."""
    return get_user_model().objects.create_user(
        **params
    )


class UserAPITest(TestCase):

    """Test Create User with Endpoint."""
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        """Test Create user."""
        payload = {
            'email': 'test@example.com',
            'password': 'test123',
            'first_name': 'rizal',
            'last_name': 'safril'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(
            email=payload['email']
        )
        self.assertTrue(user.check_password(
            payload['password']
        ))

        self.assertNotIn('password', res.data)
