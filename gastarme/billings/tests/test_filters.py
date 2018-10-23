from datetime import date
from unittest.mock import patch

from django.urls import reverse
from rest_framework import test

from users.tests.factories import UserFactory
from wallets.tests.factories import WalletFactory, CreditCardFactory
from .factories import BillFactory


class TestBillFilters(test.APITransactionTestCase):
    """Test case for the bill filters."""

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
        self.bill_one = BillFactory(
            id=1,
            credit_card=self.card_one,
            expires_at=date(2018, 10, 8)
        )
        self.bill_two = BillFactory(
            id=2,
            credit_card=self.card_two,
            expires_at=date(2018, 10, 9)
        )
        self.bill_three = BillFactory(
            id=3,
            credit_card=self.card_two,
            expires_at=date(2018, 10, 10)
        )

    @patch('billings.logger.info')
    def test_filter_expired_at_min(self, logger_mock):
        self.client.force_authenticate(self.user)

        response = self.client.get(
            reverse('billings-list'),
            {'expires_at__gte': self.bill_two.expires_at}
        )
        content = response.json()['results']
        self.assertEqual(response.json()['count'], 2)
        self.assertEqual(content[0]['id'], 2)
        self.assertEqual(content[1]['id'], 3)
        logger_mock.assert_called()

    @patch('billings.logger.info')
    def test_filter_expired_at_max(self, logger_mock):
        self.client.force_authenticate(self.user)

        response = self.client.get(
            reverse('billings-list'),
            {'expires_at__lte': self.bill_two.expires_at}
        )
        content = response.json()['results']
        self.assertEqual(response.json()['count'], 2)
        self.assertEqual(content[0]['id'], 1)
        self.assertEqual(content[1]['id'], 2)
        logger_mock.assert_called()
