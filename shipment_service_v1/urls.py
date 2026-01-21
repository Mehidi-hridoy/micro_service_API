from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShipmentV1ViewSet

router = DefaultRouter()
router.register(r'shipments', ShipmentV1ViewSet, basename='shipment-v1')

urlpatterns = [
    path('', include(router.urls)),
]
