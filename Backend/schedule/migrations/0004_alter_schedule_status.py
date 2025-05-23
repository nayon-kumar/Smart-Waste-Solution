# Generated by Django 5.2 on 2025-04-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_schedule_accepted_by_alter_schedule_requested_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('ongoing', 'Ongoing'), ('completed', 'Completed')], default='pending', max_length=20),
        ),
    ]
