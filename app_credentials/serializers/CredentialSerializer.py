from rest_framework import serializers

from smp_base_django.serializers import OwnerMixin
from smp_base_django.utils import wrap_media_errors
from utils.django.serializers.fields import ChoiceDisplayField
from utils.django.serializers.mixins import WriteableFieldsMixin

from .. import models
from ..logic import initialize

from .medium_serializers import medium_extra_credential_serializers


class CredentialSerializer(OwnerMixin, WriteableFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Credential
        fields = ('id', 'owner_id', 'medium', 'app_id', 'key', 'secret', 'extra', 'scope', 'created_at', 'updated_at')
        writable_fields = ('owner_id', 'medium', 'key', 'secret', 'extra', 'scope')

    serializer_choice_field = ChoiceDisplayField

    def validate(self, attrs):
        attrs = super().validate(attrs)
        try:
            medium_serializer = medium_extra_credential_serializers[attrs['medium']](data=attrs['extra'])
            medium_serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as exc:
            # added extra prefix to field in error message
            exc.detail = {f'extra.{field_name}': errors for field_name, errors in exc.detail.items()}
            raise exc
        except KeyError:
            pass

        return attrs

    def create(self, validated_data):
        credential = models.Credential(**validated_data)
        with wrap_media_errors():
            initialize(credential)

        credential.save()
        return credential

    def update(self, instance, validated_data):
        credential = instance

        for attr, value in validated_data.items():
            setattr(credential, attr, value)

        with wrap_media_errors():
            initialize(credential)

        credential.save()
        return credential
