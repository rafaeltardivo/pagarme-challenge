from django.db import transaction
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from rest_framework import serializers

from .models import User
from .utils import is_alpha_or_space
from .import logger


class BaseUserSerializer(serializers.ModelSerializer):
    """Base serializer for the user model."""
    password = serializers.CharField(write_only=True)

    def validate_name(self, value):
        """Validates name as alpha only."""

        if not is_alpha_or_space(value):
            raise ValidationError(
                "Must contain only alphanumeric characters"
            )
        return value

    def validate_password(self, value):
        """Validates the password according to configured validators."""

        try:
            validate_password(value, User)
        except ValidationError as error:
            raise serializers.ValidationError(error.messages)
        return value

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

        logger.info(
            'Created user {}'.format(user.email),
            extra={"user": self.context['request'].user}
        )
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
