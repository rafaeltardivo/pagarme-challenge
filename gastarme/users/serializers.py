from django.db import transaction
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from rest_framework import serializers

from .models import User


class BaseUserSerializer(serializers.ModelSerializer):
    """Base serializer for the user model."""
    password = serializers.CharField(write_only=True)

    def validate_password(self, data):
        """Validates the password according to configured validators."""

        try:
            validate_password(data, User)
        except ValidationError as error:
            raise serializers.ValidationError(error.messages)
        return data

    def create(self, validated_data, **kwargs):
        """Creates the user with the given validated data."""
        is_superuser = kwargs.pop('is_superuser', False)

        with transaction.atomic():
            user = get_user_model().objects.create(
                name=validated_data['name'],
                email=validated_data['email'],
                is_superuser=is_superuser
            )
            user.set_password(validated_data['password'])
            user.save()
        return user

    class Meta:
        model = User
        fields = ('name', 'email', 'password')


class UserSerializer(BaseUserSerializer):
    """Serializer for the regular user."""

    def create(self, validated_data, **kwargs):
        user = super().create(validated_data)
        return user


class SuperuserSerializer(BaseUserSerializer):
    """Serializer for the superuser."""
    is_superuser = serializers.CharField(read_only=True)

    def create(self, validated_data, **kwargs):
        user = super().create(validated_data, is_superuser=True)
        return user

    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'is_superuser')
