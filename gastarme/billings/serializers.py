from rest_framework import serializers

from .models import Bill


class BillSerializer(serializers.ModelSerializer):
    """Serializer for the bill model."""

    class Meta:
        model = Bill
        fields = '__all__'


class BillPaySerializer(serializers.ModelSerializer):
    """Serializer for the bill model."""

    def validate_value(self, value):
        if not value:
            raise serializers.ValidationError("Must be greater than 0.")

        return value

    class Meta:
        model = Bill
        fields = ('value', )
