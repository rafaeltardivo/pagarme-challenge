from unittest.mock import Mock, patch
from decimal import Decimal

from django.test import TestCase

from users.tests.factories import UserFactory
from wallets.tests.factories import WalletFactory, CreditCardFactory
from billings.tests.factories import BillFactory
from wallets.services import (
    new_card_update_wallet,
    new_purchase_update_wallet,
    set_payment_records,
    bill_paid_update_wallet,
    bill_paid_update_credit_card,
    card_delete_update_wallet
)


class TestWalletsServices(TestCase):
    """Test cases for billings services."""

    def setUp(self):
        self.user = UserFactory()
        self.wallet = WalletFactory(user=self.user)

    def test_new_card_update_wallet(self):

        self.assertEqual(self.wallet.credit_limit, Decimal('0.00'))

        mock_card = Mock(
            limit=Decimal('20.00'),
            available=Decimal('0.00'),
            wallet=self.wallet,
            save=Mock()
        )

        new_card_update_wallet(mock_card)
        self.assertEqual(self.wallet.credit_limit, mock_card.limit)

    @patch('purchases.models.Payment.objects.create')
    def test_new_purchase_update_wallet(self, mocked_payment):
        credit_card = CreditCardFactory(wallet=self.wallet)

        self.assertEqual(self.wallet.credit_available, Decimal('500.00'))

        mock_purchase = Mock(
            value=Decimal('20.00'),
            wallet=self.wallet
        )

        new_purchase_update_wallet(mock_purchase)

        self.assertEqual(self.wallet.credit_available, Decimal('480.00'))
        credit_card.refresh_from_db()
        self.assertEqual(credit_card.available, self.wallet.credit_available)

    @patch('purchases.models.Payment.objects.create')
    def test_set_payment_records_highest_billing_day(self, mocked_payment):
        credit_card_one = CreditCardFactory(
            wallet=self.wallet,
            number='1111111111111111',
            monthly_billing_day=8,
            limit=Decimal('50.00')
        )
        credit_card_two = CreditCardFactory(
            wallet=self.wallet,
            number='1111111111111110',
            monthly_billing_day=10,
            limit=Decimal('150.00')
        )

        mock_purchase = Mock(
            value=Decimal('50.00'),
            wallet=self.wallet
        )

        self.assertEqual(credit_card_one.available, credit_card_one.limit)
        self.assertEqual(credit_card_two.available, credit_card_two.limit)

        set_payment_records(self.wallet.credit_cards.all(), mock_purchase)

        credit_card_one.refresh_from_db()
        credit_card_two.refresh_from_db()

        self.assertEqual(credit_card_one.available, credit_card_one.limit)
        self.assertEqual(
            credit_card_two.available,
            credit_card_two.limit - mock_purchase.value
        )

    @patch('purchases.models.Payment.objects.create')
    def test_set_payment_records_lowest_limit(self, mocked_payment):
        credit_card_one = CreditCardFactory(
            wallet=self.wallet,
            number='1111111111111111',
            monthly_billing_day=10,
            limit=Decimal('150.00')
        )
        credit_card_two = CreditCardFactory(
            wallet=self.wallet,
            number='1111111111111110',
            monthly_billing_day=10,
            limit=Decimal('50.00')
        )

        mock_purchase = Mock(
            value=Decimal('50.00'),
            wallet=self.wallet
        )

        self.assertEqual(credit_card_one.available, credit_card_one.limit)
        self.assertEqual(credit_card_two.available, credit_card_two.limit)

        set_payment_records(self.wallet.credit_cards.all(), mock_purchase)

        credit_card_one.refresh_from_db()
        credit_card_two.refresh_from_db()

        self.assertEqual(credit_card_one.available, credit_card_one.limit)
        self.assertEqual(
            credit_card_two.available,
            credit_card_two.limit - mock_purchase.value
        )

    @patch('purchases.models.Payment.objects.create')
    def test_set_payment_records_split_between_cards(self, mocked_payment):
        credit_card_one = CreditCardFactory(
            wallet=self.wallet,
            number='1111111111111111',
            monthly_billing_day=10,
            limit=Decimal('50.00')
        )
        credit_card_two = CreditCardFactory(
            wallet=self.wallet,
            number='1111111111111110',
            monthly_billing_day=10,
            limit=Decimal('60.00')
        )

        mock_purchase = Mock(
            value=Decimal('100.00'),
            wallet=self.wallet
        )

        self.assertEqual(credit_card_one.available, credit_card_one.limit)
        self.assertEqual(credit_card_two.available, credit_card_two.limit)

        set_payment_records(self.wallet.credit_cards.all(), mock_purchase)

        credit_card_one.refresh_from_db()
        credit_card_two.refresh_from_db()

        self.assertEqual(credit_card_one.available, Decimal('0'))
        self.assertEqual(credit_card_two.available, Decimal('10.0'))

    def test_bill_paid_update_wallet(self):
        credit_card = CreditCardFactory(
            wallet=self.wallet,
            number='1111111111111111',
            monthly_billing_day=10,
            limit=Decimal('50.00')
        )
        bill = BillFactory(credit_card=credit_card)

        self.assertEqual(self.wallet.credit_available, Decimal('50.00'))
        bill_paid_update_wallet(bill, Decimal('100.00'))
        self.assertEqual(self.wallet.credit_available, Decimal('150.00'))

    def test_bill_paid_update_credit_card(self):
        credit_card = CreditCardFactory(
            wallet=self.wallet,
            number='1111111111111111',
            monthly_billing_day=10,
            limit=Decimal('50.00')
        )
        bill = BillFactory(credit_card=credit_card)

        self.assertEqual(credit_card.available, Decimal('50.00'))
        bill_paid_update_credit_card(bill, Decimal('100.00'))
        self.assertEqual(credit_card.available, Decimal('150.00'))

    def test_card_delete_update_wallet(self):
        credit_card = CreditCardFactory(
            wallet=self.wallet,
            number='1111111111111111',
            monthly_billing_day=10,
            limit=Decimal('50.00')
        )

        self.assertEqual(self.wallet.credit_available, Decimal('50.00'))
        card_delete_update_wallet(credit_card)
        self.assertEqual(self.wallet.credit_available, Decimal('0.00'))
