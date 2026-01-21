from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,UserHomeView

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    
    path('home/', UserHomeView.as_view(), name='user-home'),

    path('', include(router.urls)),
]
