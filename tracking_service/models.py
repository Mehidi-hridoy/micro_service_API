from django.db import models
from core.models import TimeStampedModel

class Tracking(TimeStampedModel):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('returned', 'Returned'),
    ]

    tracking_number = models.CharField(max_length=50)
    current_location = models.CharField(max_length=100)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.tracking_number} - {self.status}"
