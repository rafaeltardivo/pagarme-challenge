from rest_framework_jwt.settings import api_settings


def jwt_response_payload_handler(token, user=None, request=None):
    """Defines the response payload for JWT views."""

    return {
        'type': 'JWT',
        'token': token,
        'expires_in': api_settings.JWT_EXPIRATION_DELTA.seconds
    }
