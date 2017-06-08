"""Contact views."""
from rest_framework import viewsets
from companies.permissions import HasApiKeyPermission
from .models import (
    ContactCreator,
    ContactType,
    ContactInfo
)
from .serializers import (
    ContactCreatorSerializer,
    ContactTypeSerializer,
    ContactInfoSerializer
)


class ContactCreatorViewSet(viewsets.ModelViewSet):
    queryset = ContactCreator.objects.all()
    serializer_class = ContactCreatorSerializer


class ContactTypeViewSet(viewsets.ModelViewSet):
    queryset = ContactType.objects.all()
    serializer_class = ContactTypeSerializer


class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    permission_classes = [HasApiKeyPermission]
    authentication_classes = []
