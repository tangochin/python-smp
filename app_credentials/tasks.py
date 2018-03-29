from celery import shared_task

from smp_commons.mq import subscribe

from . import models


@subscribe('platform-auth/app:deleted')
@shared_task(ignore_result=True)
def handle_platform_app_deleted(platform_app):
    models.Credential.objects.filter(owner_id=platform_app['id']).delete()
