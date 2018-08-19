from . import serializers


def initialize(credential, request):
    smp = request.smp
    serializer = serializers.CredentialSerializer(credential)
    client = smp.get_media_client(serializer.data)

    fetched_app = client.post('v1/get-app-using-app-credential')
    if fetched_app is not None:
        app = smp.patch(f'apps/v1/by-external-id/{client.medium}:{fetched_app["external_id"]}',
                        json=fetched_app)
        credential.app_id = app['id']
    else:
        credential.app_id = None

    return credential
