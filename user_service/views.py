from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAdminUser
from .models import User
from .serializers import UserSerializer



class UserHomeView(APIView):
    def get(self, request):
        return Response({'service': 'user_service', 'status': 'running'})


class UserViewSet(
    mixins.ListModelMixin,      # GET /users/ → list all users
    mixins.RetrieveModelMixin,  # GET /users/{id}/ → get single user
    mixins.CreateModelMixin,    # POST /users/ → create new user
    mixins.UpdateModelMixin,    # PUT/PATCH /users/{id}/ → update user
    mixins.DestroyModelMixin,   # DELETE /users/{id}/ → delete user
    GenericViewSet
):
    """
    Full CRUD User API - Admin only
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]  # only superuser/admin can use these endpoints
