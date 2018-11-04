from decimal import Decimal
from purchases.models import Payment

from django.db.models import Sum

from .models import CreditCard


def set_payment_records(cards, purchase):
    """Chooses the best options for payment."""

    purchase_value = purchase.value

    for card in cards:
        available_before = card.available

        if not purchase_value:
            break

        if purchase_value > card.available:
            purchase_value -= card.available
            card.available = 0
        else:
            card.available -= purchase_value
            purchase_value = 0
        card.save()

        value = available_before - card.available
        if value:
            Payment.objects.create(
                purchase=purchase,
                credit_card=card,
                value=value
            )


def new_card_update_wallet(credit_card):
    """Updates the related wallet everytime a new card is inserted."""
    related_wallet = credit_card.wallet

    # sets the available limit
    credit_card.available = credit_card.limit
    credit_card.save()

    # updates related wallet limit and available
    if not related_wallet.credit_available:
        related_wallet.credit_available = Decimal('0.00')

    related_wallet.credit_limit += Decimal(credit_card.limit)
    related_wallet.credit_available += Decimal(credit_card.limit)
    related_wallet.save()


def new_purchase_update_wallet(purchase):
    """Updates the related wallet everytime a new purchase is made."""
    related_wallet = purchase.wallet

    cards = related_wallet.credit_cards.all()
    set_payment_records(cards, purchase)

    result = CreditCard.objects.aggregate(Sum('available'))
    related_wallet.credit_available = result['available__sum']
    related_wallet.save()


def bill_paid_update_wallet(bill, value_paid):
    """Updates the related wallet everytime a bill is paid."""
    wallet = bill.credit_card.wallet

    wallet.credit_available += value_paid
    wallet.save()


def bill_paid_update_credit_card(bill, value_paid):
    """Updates the related wallet everytime a bill is paid."""
    credit_card = bill.credit_card

    credit_card.available += value_paid
    credit_card.save()


def card_delete_update_wallet(card):
    """Updates the related wallet everytime a card is deleted."""
    wallet = card.wallet

    wallet.credit_limit -= card.limit
    wallet.credit_available -= card.available
    wallet.save()
