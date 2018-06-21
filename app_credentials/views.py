from rest_framework import viewsets
from utils.django import filters

from . import models, serializers


class CredentialFilter(filters.FilterSet):
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


class CredentialViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CredentialSerializer
    filter_class = CredentialFilter
    ordering_fields = ('created_at', )

    def get_queryset(self):
        return models.Credential.objects.filter(owner_id=self.request.auth.app_id)

    def perform_create(self, serializer):
        serializer.save(owner_id=self.request.auth.app_id)
