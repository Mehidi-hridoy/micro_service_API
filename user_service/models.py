from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('shipper', 'Shipper'),
        ('tracker', 'Tracker'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    # Fix ManyToMany clashes with default auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='service_users',  # <--- add this
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_service_users_permissions',  # <--- add this
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        db_table = 'users'
