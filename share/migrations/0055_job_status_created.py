# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-12-07 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0054_formatted_metadata_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvestjob',
            name='status',
            field=models.IntegerField(choices=[(0, 'Created'), (1, 'Started'), (2, 'Failed'), (3, 'Succeeded'), (4, 'Rescheduled'), (6, 'Forced'), (7, 'Skipped'), (8, 'Retrying'), (9, 'Cancelled')], db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='ingestjob',
            name='status',
            field=models.IntegerField(choices=[(0, 'Created'), (1, 'Started'), (2, 'Failed'), (3, 'Succeeded'), (4, 'Rescheduled'), (6, 'Forced'), (7, 'Skipped'), (8, 'Retrying'), (9, 'Cancelled')], db_index=True, default=0),
        ),
    ]
