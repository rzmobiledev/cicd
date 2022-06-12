"""
URL Mapping for Attachment.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('attachments', views.AttachmentViewSet)

app_name = 'attachment'


urlpatterns = [
    path('', include(router.urls)),
]

