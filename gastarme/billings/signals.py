from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from dateutil.relativedelta import relativedelta

from purchases.models import Payment
from .models import Bill


@receiver(post_save, sender=Payment)
def update_bill_post_payment(sender, instance, created, **kwargs):
    """ Receiver for the post-save payment signal that will update
        or generate bill for the Credit Card
    """
    next_bill_date = timezone.now().date().replace(
        day=instance.credit_card.monthly_billing_day
    ) + relativedelta(months=1)

    bill, _ = Bill.objects.get_or_create(
        credit_card=instance.credit_card,
        expires_at=next_bill_date
    )
    bill.value += instance.value
    bill.save()
