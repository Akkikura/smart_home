# Generated by Django 5.0.6 on 2024-05-11 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_measurement_sensor_alter_measurement_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
