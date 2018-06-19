from django.db import models
from django.contrib.postgres.fields import JSONField

from smp_base_django.models import Medium


class Credential(models.Model):
    owner_id = models.IntegerField()
    medium = models.SmallIntegerField(choices=Medium.as_choices())

    app_id = models.IntegerField(blank=True, null=True)

    key = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    extra = JSONField(default=dict, blank=True)
    scope = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner_id}:{self.get_medium_display()}'
