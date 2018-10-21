from unittest.mock import patch
from django.urls import reverse
from rest_framework import test
from freezegun import freeze_time

from wallets.tests.factories import WalletFactory
from users.tests.factories import UserFactory

from .factories import PurchaseFactory


class TestPurchaseFilters(test.APITransactionTestCase):
    """Test case for the purchase filters."""

    def setUp(self):
        self.user = UserFactory()
        self.wallet = WalletFactory(user=self.user)

        with freeze_time('2018-10-8'):
            self.purchase_one = PurchaseFactory(wallet=self.wallet, id=1)
        with freeze_time('2018-10-9'):
            self.purchase_two = PurchaseFactory(wallet=self.wallet, id=2)

    @patch('purchases.logger.info')
    def test_made_at_min(self, logger_mock):
        self.client.force_authenticate(self.user)

        response = self.client.get(
            reverse('purchases-list'),
            {'made_at__gte': self.purchase_one.made_at}
        )

        self.assertEqual(response.json()['count'], 2)
        logger_mock.assert_called()

    @patch('purchases.logger.info')
    def test_made_at_max(self, logger_mock):
        self.client.force_authenticate(self.user)

        response = self.client.get(
            reverse('purchases-list'),
            {'made_at__lte': self.purchase_one.made_at}
        )
        self.assertEqual(response.json()['count'], 1)
        logger_mock.assert_called()
