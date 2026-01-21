from django.contrib import admin
from .models import Shipment

@admin.register(Shipment)
class ShipmentV2Admin(admin.ModelAdmin):
    list_display = ('tracking_number', 'origin', 'destination', 'status', 'estimated_delivery', 'created_at')
    list_filter = ('status', 'origin', 'destination')
    search_fields = ('tracking_number',)
