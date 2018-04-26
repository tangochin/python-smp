from rest_framework import viewsets

from . import models, serializers


class CredentialViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CredentialSerializer

    def get_queryset(self):
        return models.Credential.objects.filter(owner_id=self.request.auth.app_id)

    def perform_create(self, serializer):
        serializer.save(owner_id=self.request.auth.app_id)
