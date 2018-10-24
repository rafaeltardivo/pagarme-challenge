from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer, SuperuserSerializer
from commons.permissions import IsSuperUser

from . import logger


class UserCreateView(CreateAPIView):
    """Create view regular users."""
    permission_classes = (AllowAny, )
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        logger.info("User create request", extra={'user': request.user})
        return super().post(request, *args, **kwargs)


class SuperuserCreateView(CreateAPIView):
    """Create view for superusers."""
    permission_classes = (IsSuperUser, )
    queryset = get_user_model().objects.all()
    serializer_class = SuperuserSerializer

    def post(self, request, *args, **kwargs):
        logger.info("Superuser create request", extra={'user': request.user})
        return super().post(request, *args, **kwargs)
