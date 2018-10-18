from unittest.mock import patch

from django.urls import reverse
from rest_framework import status, test

from purchases.models import Purchase
from wallets.tests.factories import WalletFactory, CreditCardFactory
from users.tests.factories import UserFactory


class TestPurchaseView(test.APITransactionTestCase):
    """Test cases for the user view."""

    def setUp(self):
        self.user = UserFactory()
        self.user_two = UserFactory(email='test@emailtwo.com')
        self.wallet = WalletFactory(user=self.user)
        # CreditCardFactory(wallet=self.wallet)

    def test_purchase_resource_url(self):
        self.assertEqual(reverse('purchase_create'), '/v1/purchases/')

    @patch('purchases.logger.info')
    def test_purchase_another_wallet(self, logger_mock):
        wallet = WalletFactory(user=self.user_two)
        self.client.force_authenticate(self.user)

        response = self.client.post(
            reverse('purchase_create'),
            {
                'wallet': wallet.id,
                'value': '100.00'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(
            "Wallet does not belong to current user.",
            str(response.json())
        )
        logger_mock.assert_called()

    @patch('purchases.logger.info')
    def test_purchase_without_credit_cards(self, logger_mock):
        self.client.force_authenticate(self.user)

        response = self.client.post(
            reverse('purchase_create'),
            {
                'wallet': self.wallet.id,
                'value': '100.00'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(
            "Must first have credit cards.",
            str(response.json())
        )
        logger_mock.assert_called()

    @patch('purchases.logger.info')
    def test_purchase_invalid_value(self, logger_mock):
        CreditCardFactory(wallet=self.wallet)
        self.client.force_authenticate(self.user)

        response = self.client.post(
            reverse('purchase_create'),
            {
                'wallet': self.wallet.id,
                'value': '1999.00'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(
            "Value exceeds your credit available.",
            str(response.json())
        )
        logger_mock.assert_called()

    @patch('purchases.logger.info')
    def test_purchase_create(self, logger_mock):
        CreditCardFactory(wallet=self.wallet)
        self.client.force_authenticate(self.user)

        response = self.client.post(
            reverse('purchase_create'),
            {
                'wallet': self.wallet.id,
                'value': '100.00'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Purchase.objects.count(), 1)
        logger_mock.assert_called()
