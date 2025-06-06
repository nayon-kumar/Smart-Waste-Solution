# Generated by Django 5.2 on 2025-04-21 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bin_type', models.CharField(choices=[('general', 'General Waste'), ('recyclable', 'Recyclable Waste'), ('organic', 'Organic Waste')], max_length=100)),
                ('area', models.CharField(max_length=20)),
                ('capacity', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('last_collected', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
