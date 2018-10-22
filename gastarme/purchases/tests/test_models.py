from django.test import TestCase
from freezegun import freeze_time

from purchases.models import Purchase, Payment
from .factories import PurchaseFactory, PaymentFactory
from users.tests.factories import UserFactory
from wallets.tests.factories import WalletFactory


class TestPurchaseModel(TestCase):
    """Test cases for Purchase model."""

    def setUp(self):
        with freeze_time('2018-10-10'):
            self.purchase = PurchaseFactory()

    def test_create(self):
        self.assertIsInstance(self.purchase, Purchase)

    def test_str(self):
        expected_result = (
            'Wallet: 1 value: 100.00 made_at: 2018-10-10 00:00:00'
        )
        self.assertEqual(str(self.purchase), expected_result)


class TestPaymentModel(TestCase):

    def setUp(self):
        user = UserFactory(email='test2@email.com')
        wallet = WalletFactory(user=user)
        with freeze_time('2018-10-10'):
            purchase = PurchaseFactory(wallet=wallet)
            self.payment = PaymentFactory(purchase=purchase)

    def test_create(self):
        self.assertIsInstance(self.payment, Payment)

    def test_str(self):
        expected_result = (
            'Purchase: 1 value: 100.00'
        )
        self.assertEqual(str(self.payment), expected_result)
