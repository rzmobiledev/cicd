from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from core.models import Attachment

from rest_framework import status
from rest_framework.test import APIClient


ATTACHMENT_URL = reverse('attachment:attachment-list')


def create_user(**params):
    return get_user_model().objects.create_user(**params)

def create_attachment(user, **params):
    """Create and return  a sample attachment."""

    data = {
        'title': 'Tes upload',
        'attachment': ''
    }

    data.update(params)
    attach = Attachment.objects.create(user=user, **data)
    return attach


class AttachmentTest(TestCase):
    """Testing attachment"""
    def setUp(self):
        """Create user."""
        self.client = APIClient()
        self.user = create_user(
            email='test@example.com',
            password='pass123'
        )
        self.client.force_authenticate(self.user)


class RejectIfNotAuthorized(TestCase):
    """Testing reject if not being authorized."""
    def setUp(self):
        self.client = APIClient()

    def test_to_reject_if_not_authorized(self):
        res = self.client.get(ATTACHMENT_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
