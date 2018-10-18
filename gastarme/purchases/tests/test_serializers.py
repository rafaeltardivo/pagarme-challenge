from django.test import TestCase
from rest_framework import serializers

from .factories import PurchaseFactory
from purchases.serializers import PurchaseSerializer
from users.tests.factories import UserFactory


class TestPurchaseSerializer(TestCase):
    """Test cases for Purchase model."""

    def setUp(self):
        self.user = UserFactory(email='testtwo@email.com')
        self.purchase = PurchaseFactory()
        self.purchase_serializer = PurchaseSerializer(instance=self.purchase)

    def test_wallet_content(self):
        self.assertEqual(
            self.purchase.wallet.id,
            self.purchase_serializer.data['wallet']
        )

    def test_value_content(self):
        self.assertEqual(
            str(self.purchase.value),
            self.purchase_serializer.data['value']
        )

    def test_validate_invalid_value(self):
        data = {
            'wallet': self.purchase.wallet.id,
            'value': '0'
        }

        serializer = PurchaseSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('value', serializer.errors.keys())
        self.assertIn(
            'Must be greater than 0',
            str(serializer.errors)
        )

    def test_missing_wallet(self):
        data = {
            'value': '0'
        }

        serializer = PurchaseSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('wallet', serializer.errors.keys())
        self.assertIn(
            'This field is required',
            str(serializer.errors)
        )
