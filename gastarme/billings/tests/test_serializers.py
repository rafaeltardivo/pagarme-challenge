from django.test import TestCase
from rest_framework import serializers

from billings.serializers import BillSerializer, BillPaySerializer

from .factories import BillFactory


class TestBillingsSerializer(TestCase):
    """Test cases for Billings serializer."""

    def setUp(self):
        self.bill = BillFactory()
        self.bill_serializer = BillSerializer(instance=self.bill)

    def test_credit_card_content(self):
        self.assertEqual(
            self.bill.credit_card.id,
            self.bill_serializer.data['credit_card']
        )

    def test_value_content(self):
        self.assertEqual(
            str(self.bill.value),
            self.bill_serializer.data['value']
        )

    def test_expires_at_content(self):
        self.assertEqual(
            str(self.bill.expires_at),
            self.bill_serializer.data['expires_at']
        )


class TestBillPaySerializer(TestCase):

    def test_validate_invalid_value(self):
        data = {'value': '0'}

        serializer = BillPaySerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('value', serializer.errors.keys())
        self.assertIn(
            'Must be greater than 0',
            str(serializer.errors)
        )
