from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer, SuperuserSerializer
from .permissions import IsSuperUser


class UserCreateView(CreateAPIView):
    """Create view regular users."""
    permission_classes = (AllowAny, )
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class SuperuserCreateView(CreateAPIView):
    """Create view for superusers."""
    permission_classes = (IsSuperUser, )
    queryset = get_user_model().objects.all()
    serializer_class = SuperuserSerializer
