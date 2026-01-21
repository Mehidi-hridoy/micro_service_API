from django.contrib import admin
from .models import Tracking

@admin.register(Tracking)
class TrackingAdmin(admin.ModelAdmin):
    list_display = ('tracking_number', 'current_location', 'status', 'created_at')
    list_filter = ('status', 'current_location')
    search_fields = ('tracking_number',)
