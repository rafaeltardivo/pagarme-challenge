from django.test import TestCase
from freezegun import freeze_time

from purchases.models import Purchase
from .factories import PurchaseFactory
from purchases.serializers import PurchaseSerializer


class TestPurchaseModel(TestCase):
    """Test cases for Purchase model."""

    def setUp(self):
        with freeze_time('2018-10-10'):
            self.purchase = PurchaseFactory()
        self.purchase_serializer = PurchaseSerializer(instance=self.purchase)

    def test_create(self):
        self.assertIsInstance(self.purchase, Purchase)

    def test_str(self):
        expected_result = (
            'Wallet: User: name@test.com limit: 0.00 '
            'available: None value: 100.00 made_at: 2018-10-10 00:00:00+00:00'
        )
        self.assertEqual(str(self.purchase), expected_result)
