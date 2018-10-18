from rest_framework import serializers
from .models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    """Serializer for the purchase model."""

    def validate_value(self, value):
        if not value:
            raise serializers.ValidationError("Must be greater than 0.")

        return value

    def validate_wallet(self, value):
        request = self.context.get('request')

        if request and request.user:
            try:
                if not request.user.wallet.id == value.id:
                    raise serializers.ValidationError(
                        'Wallet does not belong to current user.'
                    )
                if not request.user.wallet.credit_cards.exists():
                    raise serializers.ValidationError(
                        'Must first have credit cards.'
                    )

            except (AttributeError, ValueError):
                raise serializers.ValidationError(
                    'Must first have a wallet.'
                )

        return value

    def validate(self, data):
        request = self.context.get('request')
        value = data.get('value')

        if value > request.user.wallet.credit_available:
            raise serializers.ValidationError(
                {'value': 'Value exceeds your credit available.'}
            )

        return super().validate(data)

    class Meta:
        model = Purchase
        fields = '__all__'
