# Generated by Django 5.1.5 on 2025-01-28 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_event_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='event_participant',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
