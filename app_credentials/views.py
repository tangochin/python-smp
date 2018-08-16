from rest_framework import viewsets

from smp_base_django import filters

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


class CredentialViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CredentialSerializer
    filterset_class = CredentialFilterSet
    ordering_fields = ('created_at', )

    def get_queryset(self):
        qs = models.Credential.objects.all()
        if not self.request.auth.is_internal:
            qs = qs.filter(owner_id=self.request.auth.app_id)
        return qs

    def perform_create(self, serializer):
        serializer.save(owner_id=self.request.auth.app_id)
