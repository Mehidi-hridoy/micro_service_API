from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShipmentV2ViewSet, ShipmentV2HomeView

router = DefaultRouter()
router.register(r'shipments', ShipmentV2ViewSet, basename='shipment-v2')

urlpatterns = [
    # Landing or status page
    path('', ShipmentV2HomeView.as_view(), name='shipment-v2-home'),

    # CRUD API endpoints
    path('', include(router.urls)),
]
