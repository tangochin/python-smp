from rest_framework import serializers

from utils.django.serializers.fields import ChoiceDisplayField
from utils.django.serializers.mixins import WriteableFieldsMixin

from . import models


class CredentialSerializer(WriteableFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Credential
        fields = ('id', 'medium_id', 'key', 'secret', 'extra', 'scope', 'created_at', 'updated_at')
        writable_fields = ('medium_id', 'key', 'secret', 'extra', 'scope')

    serializer_choice_field = ChoiceDisplayField
