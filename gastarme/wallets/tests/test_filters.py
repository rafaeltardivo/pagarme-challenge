from datetime import date
from unittest.mock import patch
from rest_framework import test
from django.urls import reverse

from .factories import WalletFactory, CreditCardFactory
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
        self.credit_card_one = CreditCardFactory(
            wallet=self.wallet_one,
            id=1,
            number='1234567891011121',
            limit='300.00',
            expires_at=date(2018, 10, 10)
        )
        self.credit_card_two = CreditCardFactory(
            wallet=self.wallet_one,
            id=2,
            number='1234567891011120',
            limit='500.00',
            expires_at=date(2018, 10, 20)
        )

    @patch('wallets.logger.info')
    def test_superuser_filter_wallet_by_id(self, logger_mock):
        self.client.force_authenticate(self.super)
        response = self.client.get(
            reverse('wallets-list') + '?id={}'.format(self.wallet_two.id)
        )

        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['id'], 2)
        logger_mock.assert_called()

    @patch('wallets.logger.info')
    def test_superuser_filter_wallet_by_user(self, logger_mock):
        self.client.force_authenticate(self.super)
        response = self.client.get(
            reverse('wallets-list') + '?user={}'.format(self.user_one.id)
        )

        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['id'], 1)
        logger_mock.assert_called()

    @patch('wallets.logger.info')
    def test_superuser_filter_creditcard_by_limit_min(self, logger_mock):
        self.client.force_authenticate(self.user_one)
        url = reverse('wallet-creditcards-list', args=[self.wallet_one.id])

        response = self.client.get(
            url + '?limit_min={}'.format(self.credit_card_two.limit)
        )

        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['id'], 2)
        logger_mock.assert_called()

    @patch('wallets.logger.info')
    def test_superuser_filter_creditcard_by_limit_max(self, logger_mock):
        self.client.force_authenticate(self.user_one)
        url = reverse('wallet-creditcards-list', args=[self.wallet_one.id])

        response = self.client.get(
            url + '?limit_max={}'.format(self.credit_card_one.limit)
        )

        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['id'], 1)
        logger_mock.assert_called()

    @patch('wallets.logger.info')
    def test_superuser_filter_creditcard_by_expired_at_max(self, logger_mock):
        self.client.force_authenticate(self.user_one)
        url = reverse('wallet-creditcards-list', args=[self.wallet_one.id])

        response = self.client.get(
            url + '?expires_at_max={}'.format(self.credit_card_one.expires_at)
        )

        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['id'], 1)
        logger_mock.assert_called()
