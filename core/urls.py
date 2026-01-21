from django.urls import path
from .views import CoreHomeView

urlpatterns = [
    path('', CoreHomeView.as_view(), name='core-home'),
]
