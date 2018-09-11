from . import serializers


def initialize(credential, request):
    smp = request.smp
    medium = credential.medium.name

    fetched_app = smp.post(f'client-{medium}/v1/get-app-using-app-credential', json={
        'credential': serializers.CredentialSerializer(credential).data,
    })

    if fetched_app is not None:
        app = smp.patch(f'apps/v1/by-external-id/{medium}:{fetched_app["external_id"]}',
                        json=fetched_app)
        credential.app_id = app['id']
    else:
        credential.app_id = None

    return credential
