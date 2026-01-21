from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrackingViewSet, TrackingHomeView

router = DefaultRouter()
router.register(r'trackings', TrackingViewSet, basename='tracking')

urlpatterns = [
    path('home/', TrackingHomeView.as_view(), name='tracking-home'),
    path('', include(router.urls)),
]
