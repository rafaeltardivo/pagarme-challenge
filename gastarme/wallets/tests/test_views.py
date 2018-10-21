from datetime import date
from unittest.mock import patch

from django.urls import reverse
from rest_framework import test, status

from users.tests.factories import UserFactory
from wallets.tests.factories import CreditCardFactory, WalletFactory
from wallets.models import Wallet, CreditCard


class TestUserView(test.APITransactionTestCase):
    """Test cases for the wallet view."""

    def setUp(self):
        self.user = UserFactory(name='user', email='user@email.com')

        self.superuser = UserFactory(
            name='super',
            email='super@email.com',
            is_superuser=True
        )

    def test_user_resource_url(self):
        self.assertEqual(reverse('wallets-list'), '/v1/wallets/')
        self.assertEqual(reverse('wallets-detail', args=[1]), '/v1/wallets/1/')

    def test_superuser_resource_url(self):
        self.assertEqual(
            reverse('wallet-creditcards-list', args=[1]),
            '/v1/wallets/1/creditcards/'
        )
        self.assertEqual(
            reverse('wallet-creditcards-detail', args=[1, 1]),
            '/v1/wallets/1/creditcards/1/'
        )

    @patch('wallets.logger.info')
    def test_user_wallet_create(self, logger_mock):
        self.client.force_authenticate(self.user)

        response = self.client.post(
            reverse('wallets-list'),
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Wallet.objects.count(), 1)
        logger_mock.assert_called()

    @patch('wallets.logger.info')
    def test_user_wallet_detail(self, logger_mock):
        wallet = WalletFactory(user=self.user)
        self.client.force_authenticate(self.user)

        response = self.client.get(
            reverse('wallets-detail', args=[wallet.id]),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        logger_mock.assert_called()

    @patch('wallets.logger.info')
    def test_superuser_wallet_list(self, logger_mock):
        WalletFactory()
        WalletFactory(user=self.user)
        self.client.force_authenticate(self.superuser)

        response = self.client.get(
            reverse('wallets-list'),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 2)
        logger_mock.assert_called()

    @patch('wallets.logger.info')
    def test_superuser_wallet_delete(self, logger_mock):
        wallet = WalletFactory(user=self.user)
        self.client.force_authenticate(self.superuser)

        response = self.client.delete(
            reverse('wallets-detail', args=[wallet.id]),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        logger_mock.assert_called()

    @patch('wallets.logger.info')
    def test_user_creditcard_create(self, logger_mock):
        wallet = WalletFactory(user=self.user)
        self.client.force_authenticate(self.user)

        response = self.client.post(
            reverse('wallet-creditcards-list', args=[wallet.id]),
            {
                'wallet': wallet.id,
                'cardholder_name': 'TEST USER ONE',
                'number': '4729333912967715',
                'cvv': '999',
                'expires_at': '2022-10-30',
                'monthly_billing_day': 9,
                'limit': '900.00'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CreditCard.objects.count(), 1)
        logger_mock.assert_called()

    @patch('wallets.logger.info')
    def test_user_creditcard_list(self, logger_mock):
        wallet = WalletFactory(user=self.user)
        CreditCardFactory(
            wallet=wallet,
            number='4729333912967715',
        )
        CreditCardFactory(
            wallet=wallet,
            number='4729333922967715',
        )
        self.client.force_authenticate(self.user)

        response = self.client.get(
            reverse('wallet-creditcards-list', args=[wallet.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 2)
        logger_mock.assert_called()

    @patch('wallets.logger.info')
    def test_user_creditcard_delete(self, logger_mock):
        wallet = WalletFactory(user=self.user)
        credit_card = CreditCardFactory(
            wallet=wallet,
            number='4729333912967715',
        )
        self.client.force_authenticate(self.user)

        response = self.client.delete(
            reverse(
                'wallet-creditcards-detail',
                args=[wallet.id, credit_card.id]
            )
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        logger_mock.assert_called()
