from purchases.models import Payment


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
