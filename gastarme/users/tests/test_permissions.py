from django.urls import reverse
from rest_framework import test, status

from users.models import User


class TestUserPermissions(test.APITransactionTestCase):
    """Test cases for the permissions of the user view."""

    def test_unauthorized_superuser_create(self):
        response = self.client.post(
            reverse('superuser_create'),
            {
                'name': 'test',
                'email': 'test@email.com',
                'password': 'pass1234'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(User.objects.count(), 0)

    def test_forbidden_superuser_create(self):
        self.user = User.objects.create(
            name='super',
            email='super@email.com',
        )
        self.client.force_authenticate(self.user)

        response = self.client.post(
            reverse('superuser_create'),
            {
                'name': 'test',
                'email': 'test@email.com',
                'password': 'pass1234'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(User.objects.count(), 1)
