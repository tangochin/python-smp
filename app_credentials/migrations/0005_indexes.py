# Generated by Django 2.1 on 2018-09-14 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_credentials', '0004_auto_20180914_1456'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='credential',
            index=models.Index(fields=['owner_id'], name='app_credent_owner_i_2800c2_idx'),
        ),
        migrations.AddIndex(
            model_name='credential',
            index=models.Index(fields=['medium'], name='app_credent_medium_8e9aed_idx'),
        ),
        migrations.AddIndex(
            model_name='credential',
            index=models.Index(fields=['app_id'], name='app_credent_app_id_1b4c0b_idx'),
        ),
    ]
