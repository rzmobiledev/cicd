"""
View for attachment API
"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from . import serializers
from core.models import Attachment


class AttachmentViewSet(ModelViewSet):
    """Attachment file view."""
    serializer_class = serializers.AttachmentSerializer
    queryset = Attachment.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
