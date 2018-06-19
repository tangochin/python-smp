from smp_base_django.mq import subscribe
from smp_base_django.celery import task

from . import models


@subscribe('platform-auth/app:deleted')
@task()
def handle_platform_app_deleted(platform_app):
    models.Credential.objects.filter(owner_id=platform_app['id']).delete()
