# Generated by Django 5.2 on 2025-04-24 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestFeedback', '0003_alter_requestfeedback_status'),
        ('schedule', '0004_alter_schedule_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='request_feedback',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='requestFeedback.requestfeedback'),
        ),
    ]
