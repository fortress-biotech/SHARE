# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-10 15:34
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings

def upgrade_system_user(apps, schema_editor):
    ShareUser = apps.get_model('share', 'ShareUser')
    ShareUser.objects.filter(username=settings.APPLICATION_USERNAME).update(is_superuser=True)


def downgrade_system_user(apps, schema_editor):
    ShareUser = apps.get_model('share', 'ShareUser')
    ShareUser.objects.filter(username=settings.APPLICATION_USERNAME).update(is_superuser=False)


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0021_merged_organization_names'),
    ]

    operations = [
        migrations.RunPython(upgrade_system_user, downgrade_system_user),
    ]