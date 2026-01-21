from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Tracking
from .serializers import TrackingSerializer

class TrackingHomeView(APIView):
    def get(self, request):
        return Response({'service': 'tracking_service'})


class TrackingViewSet(ReadOnlyModelViewSet):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer
    permission_classes = [IsAuthenticated]
