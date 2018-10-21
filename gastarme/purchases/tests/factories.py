from decimal import Decimal

import factory

from purchases.models import Payment, Purchase
from wallets.tests.factories import WalletFactory, CreditCardFactory


class PurchaseFactory(factory.django.DjangoModelFactory):
    """Factory for the model Wallet."""

    class Meta:
        model = Purchase

    wallet = factory.SubFactory(WalletFactory)
    value = Decimal('100.00')


class PaymentFactory(factory.django.DjangoModelFactory):
    """Factory for the model Payment."""

    class Meta:
        model = Payment

    purchase = factory.SubFactory(PurchaseFactory)
    credit_card = factory.SubFactory(CreditCardFactory)
    value = Decimal('100.00')
