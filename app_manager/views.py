from rest_framework import viewsets

from . import models, serializers


# TODO: validate credentials on create/update (using client)
class AppViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AppSerializer

    def get_queryset(self):
        return models.App.objects.filter(owner_id=self.request.auth.app_id)

    def perform_create(self, serializer):
        serializer.save(owner_id=self.request.auth.app_id)
