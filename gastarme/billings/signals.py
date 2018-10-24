from django.dispatch import receiver
from django.db.models.signals import post_save

from purchases.models import Payment
from .services import generate_or_obtain_bill


@receiver(post_save, sender=Payment)
def update_bill_post_payment(sender, instance, created, **kwargs):
    """ Receiver for the post-save payment signal that will update
        or generate bill for the credit card
    """

    generate_or_obtain_bill(instance)
