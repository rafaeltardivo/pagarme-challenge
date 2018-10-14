from rest_framework import serializers
from django.utils import timezone

from .models import Wallet, CreditCard
from commons.utils import is_alpha_or_space


class WalletSerializer(serializers.ModelSerializer):
    """Serializer for the model Wallet."""
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    def validate_user(self, value):
        if hasattr(value, 'wallet'):
            raise serializers.ValidationError('Already has a wallet.')
        return value

    class Meta:
        model = Wallet
        fields = (
            'id',
            'credit_limit',
            'credit_available',
            'created_at',
            'user'
        )
        read_only_fields = (
            'id'
            'credit_limit',
            'credit_available',
            'created_at',
        )


class CreditCardSerializer(serializers.ModelSerializer):
    """Serializer for the model CreditCard."""

    def validate_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError('Must be only numbers.')
        if not len(value) == 16:
            raise serializers.ValidationError('Must contain 16 digits.')

        return value

    def validate_cvv(self, value):
        if not value.isdigit():
            raise serializers.ValidationError('Must be only numbers.')
        if not len(value) == 3:
            raise serializers.ValidationError('Must contain 3 digits.')

        return value

    def validate_expires_at(self, value):
        if value <= timezone.now().date():
            raise serializers.ValidationError('Card already expired.')

        return value

    def validate_cardholder_name(self, value):
        if not is_alpha_or_space(value):
            raise serializers.ValidationError('Must be letters and/or spaces.')

        return value.upper()

    def validate_monthly_billing_day(self, value):
        if value not in range(1, 21):
            raise serializers.ValidationError('Must be between days 1 and 20.')

        return value

    def validate_limit(self, value):
        if not value > 0:
            raise serializers.ValidationError('Must be greater than 0.')

        return value

    class Meta:
        model = CreditCard
        fields = ('__all__')
