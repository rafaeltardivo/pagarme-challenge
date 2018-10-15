from django.urls import path

from .views import UserCreateView, SuperuserCreateView

urlpatterns = [
    path('', UserCreateView.as_view(), name='user_create'),
    path('superusers/', SuperuserCreateView.as_view(), name='superuser_create'),
]
