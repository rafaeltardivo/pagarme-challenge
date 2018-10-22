from django.test import TestCase

from billings.models import Bill
from .factories import BillFactory


class TestBillModel(TestCase):
    """Test cases for Bill model."""

    def setUp(self):
        self.bill = BillFactory()

    def test_create(self):
        self.assertIsInstance(self.bill, Bill)

    def test_str(self):
        expected_result = 'Credit card: 1 expires_at: 2018-12-31 value: 100.00'
        self.assertEqual(str(self.bill), expected_result)
