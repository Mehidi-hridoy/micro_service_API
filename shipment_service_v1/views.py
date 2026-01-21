from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from .models import Shipment
from .serializers import ShipmentSerializer

class ShipmentV1HomeView(APIView):
    def get(self, request):
        return Response({'service': 'shipment_service', 'version': 'v1'})


class ShipmentV1ViewSet(ListModelMixin,
                        CreateModelMixin,
                        GenericViewSet):
    """
    Basic shipment API (v1)
    """
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    permission_classes = [IsAuthenticated]
