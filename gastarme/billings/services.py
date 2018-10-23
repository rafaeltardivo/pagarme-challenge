from django.dispatch import Signal
from django.utils import timezone
from dateutil.relativedelta import relativedelta

from .models import Bill

update_credit = Signal(providing_args=["value_paid", "bill"])


def pay_bill(bill, value_paid):
    """Updates bill references (wallet and card)."""

    bill.value -= value_paid
    bill.save()

    update_credit.send(bill.__class__, value_paid=value_paid, bill=bill)


def generate_or_obtain_bill(payment):
    """Generates or obtains a bill for a payment."""

    next_bill_date = timezone.now().date().replace(
        day=payment.credit_card.monthly_billing_day
    ) + relativedelta(months=1)

    bill, _ = Bill.objects.get_or_create(
        credit_card=payment.credit_card,
        expires_at=next_bill_date
    )
    bill.value += payment.value
    bill.save()
