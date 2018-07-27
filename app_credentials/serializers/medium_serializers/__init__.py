# flake8: noqa: E402, F401
from utils.registry import Registry

medium_extra_credential_serializers = Registry(key_name='medium_id')

from .ok import OkMidiumExtraCredentialSerializer
