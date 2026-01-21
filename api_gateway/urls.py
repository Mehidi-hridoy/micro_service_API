from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api/users/', include('user_service.urls')),
    path('api/shipment/v1/', include('shipment_service_v1.urls')),
    path('api/shipment/v2/', include('shipment_service_v2.urls')),
    path('api/tracking/', include('tracking_service.urls')),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
