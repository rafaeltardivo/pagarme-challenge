from django.urls import path

from .views import UserCreateView, SuperuserCreateView

urlpatterns = [
    path('', UserCreateView.as_view(), name='user_create'),
    path('superuser/', SuperuserCreateView.as_view(), name='staff_create'),
]
