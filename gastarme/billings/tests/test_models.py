from datetime import date

from django.test import TestCase
from django.db import IntegrityError

from billings.models import Bill
from wallets.tests.factories import CreditCardFactory, WalletFactory
from users.tests.factories import UserFactory

from .factories import BillFactory


class TestBillModel(TestCase):
    """Test cases for Bill model."""

    def setUp(self):
        self.user = UserFactory()
        self.wallet = WalletFactory(user=self.user)
        self.credit_card = CreditCardFactory(
            wallet=self.wallet,
            number='4729333912967716'
        )
        self.bill = BillFactory(credit_card=self.credit_card)

    def test_create(self):
        self.assertIsInstance(self.bill, Bill)

    def test_str(self):
        expected_result = 'Credit card: 1 expires_at: 2018-12-31 value: 100.00'
        self.assertEqual(str(self.bill), expected_result)

    def test_unique_monthly_bill(self):
        bill_date = date(2018, 10, 10)
        BillFactory(
            credit_card=self.credit_card,
            expires_at=bill_date
        )

        with self.assertRaises(IntegrityError):
            BillFactory(
                credit_card=self.credit_card,
                expires_at=bill_date
            )
