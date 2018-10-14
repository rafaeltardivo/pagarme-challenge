from django.urls import reverse
from rest_framework import test, status

from users.models import User
from wallets.models import Wallet


class TestWalletPermissions(test.APITransactionTestCase):
    """Test cases for the permissions of the wallets view."""

    def setUp(self):
        self.user = User.objects.create(
            name='user',
            email='user@email.com',
        )

        self.superuser = User.objects.create(
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
        wallet = Wallet.objects.create(
            user=self.user
        )
        self.client.force_authenticate(self.superuser)

        response = self.client.put(
            reverse('wallets-detail', args=[wallet.id])
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_forbidden_user_wallet_delete(self):
        wallet = Wallet.objects.create(
            user=self.user
        )
        self.client.force_authenticate(self.user)

        response = self.client.delete(
            reverse('wallets-detail', args=[wallet.id])
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
