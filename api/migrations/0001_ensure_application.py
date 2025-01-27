# Generated by Django 3.2.5 on 2021-07-12 23:23

from django.db import migrations
from django.conf import settings


def ensure_application(apps, schema_editor):
    from oauth2_provider.models import Application as ActualApplication
    Application = apps.get_model('oauth2_provider', 'Application')
    ShareUser = apps.get_model('share', 'ShareUser')
    share_user = ShareUser.objects.get(username=settings.APPLICATION_USERNAME)
    Application.objects.get_or_create(
        client_type=str(ActualApplication.CLIENT_TYPES[0][1]),
        authorization_grant_type=str(ActualApplication.GRANT_TYPES[2][1]),
        name='Harvester API',
        user=share_user
    )


class Migration(migrations.Migration):

    replaces = [
        ('api', '0001_create_application'),
    ]

    dependencies = [
        ('oauth2_provider', '0002_08_updates'),
        ('share', '0061_ensure_auto_users'),
    ]

    operations = [
        migrations.RunPython(ensure_application),
    ]
