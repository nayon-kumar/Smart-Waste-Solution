# Generated by Django 5.2 on 2025-05-01 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0010_alter_vehicle_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='license_no',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
