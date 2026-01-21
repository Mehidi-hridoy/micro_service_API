from django.db import models
from core.models import TimeStampedModel

class Shipment(TimeStampedModel):
    tracking_number = models.CharField(max_length=50, unique=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    estimated_delivery = models.DateField(null=True, blank=True)
