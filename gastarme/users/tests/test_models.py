from django.test import TestCase

from users.models import User
from .factories import UserFactory


class UserModelTestCase(TestCase):
    """Test cases for User model."""

    def test_create(self):
        user = UserFactory(password='testpass123')

        self.assertIsInstance(user, User)

    def test_str(self):
        expected_result = 'name@test.com'
        user = UserFactory(password='testpass123')

        self.assertEqual(str(user), expected_result)
