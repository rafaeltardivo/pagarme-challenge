from django.dispatch import Signal

update_debt = Signal(providing_args=["value_paid", "bill"])


def pay_bill(bill, value_paid):
    """Updates bill references (wallet and card)."""

    bill.value -= value_paid
    bill.save()

    update_debt.send(bill.__class__, value_paid=value_paid, bill=bill)
