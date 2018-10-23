from unittest.mock import patch
from django.urls import reverse
from rest_framework import test, status

from users.tests.factories import UserFactory
from wallets.tests.factories import WalletFactory, CreditCardFactory

from .factories import BillFactory


class TestBillingsView(test.APITransactionTestCase):
    """Test cases for the billing view."""

    def setUp(self):
        self.user = UserFactory()
        self.wallet = WalletFactory(user=self.user)
        self.card_one = CreditCardFactory(
            wallet=self.wallet,
            number='4916293874816172'
        )
        self.card_two = CreditCardFactory(
            wallet=self.wallet,
            number='4349469061007652'
        )

    def test_billings_resource_url(self):
        self.assertEqual(reverse('billings-list'), '/v1/billings/')
        self.assertEqual(
            reverse('billings-detail', args=[1]), '/v1/billings/1/'
        )

    def test_pay_resource_url(self):
        self.assertEqual(
            reverse('billings-pay', args=[1]), '/v1/billings/1/pay/'
        )

    @patch('billings.logger.info')
    def test_billings_list(self, logger_mock):
        self.client.force_authenticate(self.user)
        BillFactory(credit_card=self.card_one)
        BillFactory(credit_card=self.card_two)

        response = self.client.get(reverse('billings-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 2)
        logger_mock.assert_called()

    @patch('billings.logger.info')
    def test_billings_detail(self, logger_mock):
        self.client.force_authenticate(self.user)
        bill = BillFactory(credit_card=self.card_one)

        response = self.client.get(reverse('billings-detail', args=[bill.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['id'], bill.id)
        logger_mock.assert_called()

    @patch('billings.logger.info')
    def test_billings_pay_bill(self, logger_mock):
        self.client.force_authenticate(self.user)
        bill = BillFactory(credit_card=self.card_one)

        response = self.client.patch(
            reverse('billings-pay', args=[bill.id]),
            {'value': '25.00'}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['id'], bill.id)
        logger_mock.assert_called()
