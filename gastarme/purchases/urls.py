from django.urls import path
from .views import PurchaseCreateView


urlpatterns = [
    path('', PurchaseCreateView.as_view(), name='purchase_create'),
]
