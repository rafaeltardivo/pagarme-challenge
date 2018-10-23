from decimal import Decimal

from unittest.mock import patch

from django.test import TestCase
from django.db.models.signals import post_save

from wallets.models import CreditCard
from purchases.models import Purchase
from purchases.tests.factories import PurchaseFactory
from users.tests.factories import UserFactory
from wallets.tests.factories import WalletFactory, CreditCardFactory
from billings.services import update_credit, pay_bill
from billings.models import Bill
from billings.tests.factories import BillFactory


class TestWalletssSignals(TestCase):
    """Test cases for wallets signals."""

    def setUp(self):
        self.user = UserFactory(email='test@email.com')
        self.wallet = WalletFactory(user=self.user)

    @patch('wallets.signals.update_wallet_post_create_card', autospec=True)
    def test_update_bill_post_payment(self, mocked_handler):

        post_save.connect(
            mocked_handler,
            sender=CreditCard,
            dispatch_uid='test_handler'
        )

        CreditCardFactory(wallet=self.wallet)

        self.assertTrue(mocked_handler.called)
        self.assertEquals(mocked_handler.call_count, 2)

    @patch('wallets.signals.update_wallet_post_purchase', autospec=True)
    def test_update_wallet_post_purchase(self, mocked_handler):

        post_save.connect(
            mocked_handler,
            sender=Purchase,
            dispatch_uid='test_handler'
        )

        PurchaseFactory(wallet=self.wallet)

        self.assertTrue(mocked_handler.called)
        self.assertEquals(mocked_handler.call_count, 1)

    @patch('wallets.signals.update_credit_post_bill_paid', autospec=True)
    def test_update_credit_post_bill_paid(self, mocked_handler):

        update_credit.connect(
            mocked_handler,
            sender=Bill,
            dispatch_uid='test_handler'
        )
        bill = BillFactory(credit_card=CreditCardFactory(wallet=self.wallet))
        pay_bill(bill, Decimal('100.00'))

        self.assertTrue(mocked_handler.called)
        self.assertEquals(mocked_handler.call_count, 1)
