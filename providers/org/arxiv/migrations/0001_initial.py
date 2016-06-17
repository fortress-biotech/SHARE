# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 04:07
from __future__ import unicode_literals

from django.db import migrations
import share.core.provider


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            code=share.core.provider.ProviderSourceMigration('arxiv'),
        ),
        migrations.RunPython(
            code=share.core.provider.HarvesterScheduleMigration('arxiv'),
        ),
        migrations.RunPython(
            code=share.core.provider.NormalizerScheduleMigration('arxiv'),
        ),
    ]