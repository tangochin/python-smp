from rest_framework import viewsets

from smp_base_django import filters
from smp_base_django.views import OwnerMixin

from . import models, serializers


class CredentialFilterSet(filters.FilterSet):
    class Meta:
        model = models.Credential
        fields = {
            'id': ['exact', 'in'],

            'created_at': ['exact', 'isnull', 'gt', 'gte', 'lt', 'lte'],
            'updated_at': ['exact', 'isnull', 'gt', 'gte', 'lt', 'lte'],

            'medium': ['exact'],
            'key': ['exact'],
            'app_id': ['exact', 'in'],
        }


class CredentialViewSet(OwnerMixin, viewsets.ModelViewSet):
    queryset = models.Credential.objects.all()
    serializer_class = serializers.CredentialSerializer
    filterset_class = CredentialFilterSet
    ordering_fields = ('created_at', )
