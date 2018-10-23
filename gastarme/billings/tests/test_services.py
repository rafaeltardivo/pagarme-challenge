from decimal import Decimal

from django.test import TestCase

from freezegun import freeze_time

from billings.tests.factories import BillFactory
from billings.services import pay_bill, generate_or_obtain_bill
from billings.models import Bill
from users.tests.factories import UserFactory
from wallets.tests.factories import WalletFactory, CreditCardFactory
from purchases.models import Payment


class TestBillingsServices(TestCase):
    """Test cases for billings services."""

    def test_pay_bill_service(self):
        bill = BillFactory()
        credit_card = bill.credit_card
        wallet = credit_card.wallet

        self.assertEqual(credit_card.available, Decimal('500.00'))
        self.assertEqual(wallet.credit_available, Decimal('500.00'))

        pay_bill(bill, Decimal('50.00'))

        self.assertEqual(credit_card.available, Decimal('550.00'))
        self.assertEqual(wallet.credit_available, Decimal('550.00'))

    def test_generate_bill_next_month(self):
        user = UserFactory()
        wallet = WalletFactory(user=user)
        credit_card = CreditCardFactory(wallet=wallet)

        with freeze_time('2018-10-10'):
            payment_value = Decimal('200.00')
            payment = Payment(
                purchase=None,
                credit_card=credit_card,
                value=payment_value
            )

            generate_or_obtain_bill(payment)

            self.assertEqual(Bill.objects.count(), 1)

            generated_bill = Bill.objects.get(id=1)
            self.assertEqual(generated_bill.value, payment_value)
            self.assertEqual(generated_bill.expires_at.month, 11)

    def test_obtain_bill_next_month(self):
        user = UserFactory()
        wallet = WalletFactory(user=user)
        credit_card = CreditCardFactory(wallet=wallet)

        with freeze_time('2018-10-10'):
            payment_value = Decimal('200.00')
            payment = Payment(
                purchase=None,
                credit_card=credit_card,
                value=payment_value
            )
            payment_two = Payment(
                purchase=None,
                credit_card=credit_card,
                value=payment_value
            )

            generate_or_obtain_bill(payment)
            generate_or_obtain_bill(payment_two)
            self.assertEqual(Bill.objects.count(), 1)

            generated_bill = Bill.objects.get(id=1)
            self.assertEqual(generated_bill.value, payment_value * 2)
            self.assertEqual(generated_bill.expires_at.month, 11)
