from django.contrib import admin
from .models import TimeStampedModel  # Only if you have real models

# TimeStampedModel is abstract; no need to register
# Example: if you had a real model
# @admin.register(YourCoreModel)
# class YourCoreModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'created_at', 'updated_at')
#     search_fields = ('id',)
