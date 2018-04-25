from rest_framework import serializers

from smp_commons.utils import wrap_media_errors
from utils.django.serializers.fields import ChoiceDisplayField
from utils.django.serializers.mixins import WriteableFieldsMixin

from . import models
from .logic import initialize


class CredentialSerializer(WriteableFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Credential
        fields = ('id', 'medium_id', 'app_id', 'key', 'secret', 'extra', 'scope', 'created_at', 'updated_at')
        writable_fields = ('medium_id', 'key', 'secret', 'extra', 'scope')

    serializer_choice_field = ChoiceDisplayField

    def create(self, validated_data):
        credential = models.Credential(**validated_data)
        with wrap_media_errors():
            return initialize(credential)

    def update(self, instance, validated_data):
        credential = instance

        for attr, value in validated_data.items():
            setattr(credential, attr, value)

        with wrap_media_errors():
            return initialize(credential)
