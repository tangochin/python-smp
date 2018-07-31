# flake8: noqa: E402, F401
from ...utils.registry import MediumSerializersRegistry

medium_extra_credential_serializers = MediumSerializersRegistry(key_name='medium_id')

from .ok import OkMidiumExtraCredentialSerializer
