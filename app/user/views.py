"""
Views for user API
"""
from rest_framework import (
    generics,
    permissions,
    authentication,
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from . import serializers


class CreateUserView(generics.CreateAPIView):
    """Create a new user inside the database."""
    serializer_class = serializers.UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create Token for authenticated users"""
    serializer_class = serializers.AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Retrieve user data and update."""
    serializer_class = serializers.UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Return or retrieve user information"""
        return self.request.user
