from unittest.mock import patch

from django.test import TestCase
from django.db.models.signals import post_save

from purchases.models import Payment
from purchases.tests.factories import PurchaseFactory, PaymentFactory
from users.tests.factories import UserFactory
from wallets.tests.factories import WalletFactory


class TestBillingsSignals(TestCase):
    """Test cases for signals."""

    def setUp(self):
        self.user = UserFactory(email='test@email.com')
        self.wallet = WalletFactory(user=self.user)
        self.purchase = PurchaseFactory(wallet=self.wallet)

    @patch('billings.signals.update_bill_post_payment', autospec=True)
    def test_update_bill_post_payment(self, mocked_handler):

        post_save.connect(
            mocked_handler,
            sender=Payment,
            dispatch_uid='test_handler'
        )

        PaymentFactory(purchase=self.purchase)

        self.assertTrue(mocked_handler.called)
        self.assertEquals(mocked_handler.call_count, 1)
