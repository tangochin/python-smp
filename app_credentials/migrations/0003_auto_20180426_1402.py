# Generated by Django 2.0.4 on 2018-04-26 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_credentials', '0002_credential_app_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credential',
            old_name='medium_id',
            new_name='medium',
        ),
    ]
