from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Shipment
from .serializers import ShipmentSerializer

class ShipmentV2HomeView(APIView):
    def get(self, request):
        return Response({'service': 'shipment_service', 'version': 'v2'})


class ShipmentV2ViewSet(ModelViewSet):
    """
    Full CRUD shipment API (v2)
    """
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(status='created_v2')
