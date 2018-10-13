from django.test import TestCase

from wallets.models import Wallet, CreditCard
from .factories import WalletFactory, CreditCardFactory


class WalletModelTestCase(TestCase):
    """Test cases for Wallet model."""

    def test_create(self):
        wallet = WalletFactory()

        self.assertIsInstance(wallet, Wallet)

    def test_str(self):
        expected_result = 'User: name@test.com limit: 750.00 available: 350.00'
        wallet = WalletFactory()

        self.assertEqual(str(wallet), expected_result)


class CreditCardModelTestCase(TestCase):
    """Test cases for CreditCard model."""

    def test_create(self):
        credit_card = CreditCardFactory()

        self.assertIsInstance(credit_card, CreditCard)

    def test_str(self):
        expected_result = ('Wallet: User: name@test.com limit: 750.00 '
                           'available: 350.00 number: 4729333912967716 '
                           'limit: 500.00 monthly_billing_day: 10')
        credit_card = CreditCardFactory(number='4729333912967716')

        self.assertEqual(str(credit_card), expected_result)
