from unittest.mock import patch

from django.urls import reverse
from rest_framework import test, status

from users.tests.factories import UserFactory
from wallets.tests.factories import WalletFactory
from wallets.models import Wallet, CreditCard


class TestWalletPermissions(test.APITransactionTestCase):
    """Test cases for the permissions of the wallets view."""

    def setUp(self):
        self.user = UserFactory(name='user', email='user@email.com')

        self.superuser = UserFactory(
            name='super',
            email='super@email.com',
            is_superuser=True
        )

    def test_forbidden_superuser_wallet_create(self):
        self.client.force_authenticate(self.superuser)

        response = self.client.post(
            reverse('wallets-list')
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Wallet.objects.count(), 0)

    def test_forbidden_superuser_wallet_update(self):
        wallet = WalletFactory(user=self.user)
        self.client.force_authenticate(self.superuser)

        response = self.client.put(
            reverse('wallets-detail', args=[wallet.id])
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_forbidden_user_wallet_delete(self):
        wallet = WalletFactory(user=self.user)
        self.client.force_authenticate(self.user)

        response = self.client.delete(
            reverse('wallets-detail', args=[wallet.id])
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @patch('wallets.logger.info')
    def test_user_unauthorized_wallet(self, logger_mock):
        wallet = WalletFactory(user=self.user)
        self.client.force_authenticate(self.user)

        response = self.client.post(
            reverse('creditcards-list'),
            {
                'wallet': wallet.id + 1,
                'cardholder_name': 'TEST USER ONE',
                'number': '4729333912967715',
                'cvv': '999',
                'expires_at': '2022-10-30',
                'monthly_billing_day': 9,
                'limit': '900.00'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        logger_mock.assert_called()
