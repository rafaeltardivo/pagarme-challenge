from django.test import TestCase
from rest_framework import serializers

from users.serializers import UserSerializer
from .factories import UserFactory


class TestUserSerializer(TestCase):
    """Test cases for the user serializer."""

    def setUp(self):
        self.user = UserFactory()
        self.user_serializer = UserSerializer(instance=self.user)

    def test_name_content(self):
        self.assertEqual(self.user.name, self.user_serializer.data['name'])

    def test_email_content(self):
        self.assertEqual(self.user.email, self.user_serializer.data['email'])

    def test_validate_name(self):
        data = {
            'name': 'j0hn',
            'email': 'valid@email.com',
            'password': 'pass1234'
        }
        serializer = UserSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('name', serializer.errors.keys())

    def test_validate_email(self):
        data = {
            'name': 'John',
            'email': 'invalidemail.com',
            'password': 'pass1234'
        }
        serializer = UserSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('email', serializer.errors.keys())

    def test_validate_password(self):
        data = {
            'name': 'John',
            'email': 'valid@email.com',
            'password': 'pass'
        }
        serializer = UserSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('password', serializer.errors.keys())

    def test_valid_data(self):
        data = {
            'name': 'John',
            'email': 'valid@email.com',
            'password': 'pass1234'
        }

        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
