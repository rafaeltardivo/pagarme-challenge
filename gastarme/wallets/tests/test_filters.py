from unittest.mock import patch
from rest_framework import test
from django.urls import reverse

from .factories import WalletFactory
from users.tests.factories import UserFactory


class TestWalletSerializer(test.APITransactionTestCase):
    """Test cases for the Wallet serializer."""

    def setUp(self):
        self.super = UserFactory(
            email='super@email.com',
            is_superuser=True
        )
        self.user_one = UserFactory(id=98, email='abc@email.com')
        self.user_two = UserFactory(id=99, email='bcd@email.com')
        self.wallet_one = WalletFactory(user=self.user_one, id=1)
        self.wallet_two = WalletFactory(user=self.user_two, id=2)

    @patch('wallets.logger.info')
    def test_superuser_filter_by_id(self, logger_mock):
        self.client.force_authenticate(self.super)
        response = self.client.get(
            reverse('wallets-list') + '?id={}'.format(self.wallet_two.id)
        )

        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['id'], 2)
        logger_mock.assert_called()

    @patch('wallets.logger.info')
    def test_superuser_filter_by_user(self, logger_mock):
        self.client.force_authenticate(self.super)
        response = self.client.get(
            reverse('wallets-list') + '?user={}'.format(self.user_one.id)
        )

        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['id'], 1)
        logger_mock.assert_called()
