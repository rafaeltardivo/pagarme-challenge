from django.conf.urls import url, include
from rest_framework_nested import routers

from .views import PurchaseViewSet

router = routers.SimpleRouter()
router.register('', PurchaseViewSet, base_name='purchases')

urlpatterns = [
    url('', include(router.urls)),
]
