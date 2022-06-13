"""
Serializer API for Attachment
"""
from rest_framework.serializers import ModelSerializer
from core import models


class AttachmentSerializer(ModelSerializer):
    class Meta:
        model = models.Attachment
        fields = ['title', 'attachment']
