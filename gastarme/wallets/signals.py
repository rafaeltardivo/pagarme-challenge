from django.dispatch import receiver
from django.db.models.signals import post_save

from billings.services import update_credit
from purchases.models import Purchase
from .models import CreditCard
from .services import (
    new_card_update_wallet,
    new_purchase_update_wallet,
    bill_paid_update_wallet,
    bill_paid_update_credit_card
)


@receiver(post_save, sender=CreditCard)
def update_wallet_post_create_card(sender, instance, created, **kwargs):
    """Receiver for the Creditcard post-save signal that will update
       the CreditCard itself and it's related Wallet.
    """

    if created:
        new_card_update_wallet(instance)


@receiver(post_save, sender=Purchase)
def update_wallet_post_purchase(sender, instance, **kwargs):
    """Receiver for the Purchase post-save signal that will update
       credit limits.
    """

    new_purchase_update_wallet(instance)


@receiver(update_credit)
def update_credit_post_bill_paid(sender, bill, value_paid, **kwargs):
    """Receiver for the  update_debt signal (post bill payment) that will
       update the related wallet.
    """

    bill_paid_update_wallet(bill, value_paid)
    bill_paid_update_credit_card(bill, value_paid)
