from rest_framework import serializers
from .models import TimeStampedModel

# Example serializer for demonstration (core doesn't have DB table by default)
class CoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeStampedModel  # abstract model, can be used for inheritance
        fields = ['created_at', 'updated_at']
