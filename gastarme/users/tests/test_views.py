from unittest.mock import patch

from django.urls import reverse
from rest_framework import test, status

from users.models import User


class TestUserView(test.APITransactionTestCase):
    """Test cases for the user view."""

    def test_user_resource_url(self):
        self.assertEqual(reverse('user_create'), '/v1/users/')

    def test_superuser_resource_url(self):
        self.assertEqual(reverse('superuser_create'), '/v1/users/superuser/')

    @patch('users.logger.info')
    def test_user_creation(self, logger_mock):
        response = self.client.post(
            reverse('user_create'),
            {
                'name': 'test',
                'email': 'test@email.com',
                'password': 'pass1234'
            },
            format='json'
        )
        logger_mock.assert_called()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_unauthorized_superuser_creation(self):
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

    def test_forbidden_superuser_creation(self):
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

    @patch('users.logger.info')
    def test_superuser_creation(self, logger_mock):
        self.superuser = User.objects.create(
            name='super',
            email='super@email.com',
            is_superuser=True
        )
        self.client.force_authenticate(self.superuser)

        response = self.client.post(
            reverse('superuser_create'),
            {
                'name': 'test',
                'email': 'test@email.com',
                'password': 'pass1234'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        logger_mock.assert_called()
