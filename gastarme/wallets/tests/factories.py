from datetime import date
from decimal import Decimal

import factory

from wallets.models import CreditCard, Wallet
from users.tests.factories import UserFactory


class WalletFactory(factory.django.DjangoModelFactory):
    """Factory for the model Wallet."""

    class Meta:
        model = Wallet

    user = factory.SubFactory(UserFactory)
    credit_limit = Decimal('750.00')
    credit_available = Decimal('350.00')


class CreditCardFactory(factory.django.DjangoModelFactory):
    """ Factory for the model CreditCard """

    class Meta:
        model = CreditCard

    wallet = factory.SubFactory(WalletFactory)
    number = '4729333912967715'
    cardholder_name = "TEST USER CARD"
    cvv = '333'
    expires_at = date(2022, 10, 30)
    monthly_billing_day = 10
    limit = Decimal('500.00')
    is_active = True
