from django.test import TestCase

from rest_framework import serializers
from freezegun import freeze_time

from .factories import WalletFactory, CreditCardFactory
from wallets.serializers import WalletSerializer, CreditCardSerializer


class TestWalletSerializer(TestCase):
    """Test cases for the Wallet serializer."""

    def setUp(self):
        self.wallet = WalletFactory()
        self.wallet_serializer = WalletSerializer(instance=self.wallet)

    def test_name_content(self):
        self.assertEqual(
            self.wallet.user.id,
            self.wallet_serializer.data['user'])

    def test_credit_limit_content(self):
        self.assertEqual(
            str(self.wallet.credit_limit),
            self.wallet_serializer.data['credit_limit']
        )

    def test_credit_available_content(self):
        self.assertEqual(
            str(self.wallet.credit_available),
            self.wallet_serializer.data['credit_available']
        )


class TestCreditCardSerializer(TestCase):
    """Test cases for the CreditCard serializer."""

    def setUp(self):
        self.credit_card = CreditCardFactory()
        self.credit_card_serializer = CreditCardSerializer(
            instance=self.credit_card
        )

    def test_number_content(self):
        self.assertEqual(
            self.credit_card.number,
            self.credit_card_serializer.data['number']
        )

    def test_cardholder_name_content(self):
        self.assertEqual(
            self.credit_card.cardholder_name,
            self.credit_card_serializer.data['cardholder_name']
        )

    def test_cvv_content(self):
        self.assertEqual(
            self.credit_card.cvv,
            self.credit_card_serializer.data['cvv']
        )

    def test_expires_at_content(self):
        self.assertEqual(
            str(self.credit_card.expires_at),
            self.credit_card_serializer.data['expires_at']
        )

    def test_monthly_billing_day_content(self):
        self.assertEqual(
            self.credit_card.monthly_billing_day,
            self.credit_card_serializer.data['monthly_billing_day']
        )

    def test_limit_content(self):
        self.assertEqual(
            str(self.credit_card.limit),
            self.credit_card_serializer.data['limit']
        )

    def test_is_active_content(self):
        self.assertEqual(
            self.credit_card.is_active,
            self.credit_card_serializer.data['is_active']
        )

    def test_validate_number_length(self):
        data = {
            'wallet': 1,
            'cardholder_name': 'TEST USER ONE',
            'number': '472933391296771',
            'cvv': '999',
            'expires_at': '2022-10-30',
            'monthly_billing_day': 9,
            'limit': '900.00'
        }
        serializer = CreditCardSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('number', serializer.errors.keys())
        self.assertIn('Must contain 16 digits', str(serializer.errors))

    def test_validate_number_only_digits(self):
        data = {
            'wallet': 1,
            'cardholder_name': 'TEST USER ONE',
            'number': '472933391296771A',
            'cvv': '999',
            'expires_at': '2022-10-30',
            'monthly_billing_day': 9,
            'limit': '900.00'
        }
        serializer = CreditCardSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('number', serializer.errors.keys())
        self.assertIn('Must be only numbers', str(serializer.errors))

    def test_validate_cvv_length(self):
        data = {
            'wallet': 1,
            'cardholder_name': 'TEST USER ONE',
            'number': '4729333912967715',
            'cvv': '99',
            'expires_at': '2022-10-30',
            'monthly_billing_day': 9,
            'limit': '900.00'
        }
        serializer = CreditCardSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('cvv', serializer.errors.keys())
        self.assertIn('Must contain 3 digits', str(serializer.errors))

    def test_validate_cvv_only_digits(self):
        data = {
            'wallet': 1,
            'cardholder_name': 'TEST USER ONE',
            'number': '4729333912967715',
            'cvv': '99A',
            'expires_at': '2022-10-30',
            'monthly_billing_day': 9,
            'limit': '900.00'
        }
        serializer = CreditCardSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('cvv', serializer.errors.keys())
        self.assertIn('Must be only numbers', str(serializer.errors))

    def test_validate_cardholder_only_alpha(self):
        data = {
            'wallet': 1,
            'cardholder_name': 'TEST 1SER ONE',
            'number': '4729333912967715',
            'cvv': '999',
            'expires_at': '2022-10-30',
            'monthly_billing_day': 9,
            'limit': '900.00'
        }
        serializer = CreditCardSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('cardholder_name', serializer.errors.keys())
        self.assertIn('Must be letters and/or spaces', str(serializer.errors))

    def test_validate_monthly_billing_day(self):
        data = {
            'wallet': 1,
            'cardholder_name': 'TEST USER ONE',
            'number': '4729333912967715',
            'cvv': '999',
            'expires_at': '2022-10-30',
            'monthly_billing_day': 21,
            'limit': '900.00'
        }
        serializer = CreditCardSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('monthly_billing_day', serializer.errors.keys())
        self.assertIn('Must be between days 1 and 20', str(serializer.errors))

    def test_validate_limit(self):
        data = {
            'wallet': 1,
            'cardholder_name': 'TEST USER ONE',
            'number': '4729333912967715',
            'cvv': '999',
            'expires_at': '2022-10-30',
            'monthly_billing_day': 20,
            'limit': '0.00'
        }
        serializer = CreditCardSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('limit', serializer.errors.keys())
        self.assertIn('Must be greater than 0', str(serializer.errors))

    def test_validate_expires_at(self):
        data = {
            'wallet': 1,
            'cardholder_name': 'TEST USER ONE',
            'number': '4729333912967715',
            'cvv': '999',
            'expires_at': '2018-10-10',
            'monthly_billing_day': 20,
            'limit': '900.00'
        }

        with freeze_time('2018-10-01'):
            serializer = CreditCardSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('expires_at', serializer.errors.keys())
        self.assertIn('Card already expired', str(serializer.errors))
