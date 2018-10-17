from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('jwt/obtain/', obtain_jwt_token, name='obtain_jwt'),
    path('jwt/refresh/', refresh_jwt_token, name='refresh_jwt'),
]
