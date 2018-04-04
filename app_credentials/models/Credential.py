from django.db import models
from django.contrib.postgres.fields import JSONField

from smp_commons.models import Medium


class Credential(models.Model):
    owner_id = models.IntegerField()
    medium_id = models.SmallIntegerField(choices=Medium.as_choices())

    key = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    extra = JSONField(default=dict, blank=True)
    scope = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}:{}'.format(self.owner_id, self.medium)

    @property
    def medium(self):
        return self.get_medium_id_display()
