from rest_framework import serializers

from smp_base_django.models import Medium

from . import medium_extra_credential_serializers


@medium_extra_credential_serializers.register
class OkMidiumExtraCredentialSerializer(serializers.Serializer):
    medium_id = Medium.ok

    external_id = serializers.IntegerField(required=True)
