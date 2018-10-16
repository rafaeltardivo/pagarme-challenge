from rest_framework import test
from django.urls import reverse

from .factories import WalletFactory
from users.tests.factories import UserFactory


class TestWalletSerializer(test.APITransactionTestCase):
    """Test cases for the Wallet serializer."""

    def setUp(self):
        self.super = UserFactory(email='super@email.com')
        self.user_one = UserFactory(id=98, email='abc@email.com')
        self.user_two = UserFactory(id=99, email='bcd@email.com')
        self.wallet_one = WalletFactory(user=self.user_one)
        self.wallet_two = WalletFactory(user=self.user_two)

    def test_filter_by_id(self):
        self.client.force_authenticate(self.super)
        url = reverse('wallets-list')
        response = self.client.get(url + '?user={}'.format(self.user_one.id))


