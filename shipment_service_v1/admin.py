from django.contrib import admin
from .models import Shipment

@admin.register(Shipment)
class ShipmentV1Admin(admin.ModelAdmin):
    list_display = ('tracking_number', 'origin', 'destination', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'origin', 'destination')
    search_fields = ('tracking_number', 'origin', 'destination')
    ordering = ('-created_at',)
