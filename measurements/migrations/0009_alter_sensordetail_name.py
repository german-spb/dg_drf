# Generated by Django 4.1.7 on 2023-03-26 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0008_rename_sensor_sensordetail_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordetail',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurements.measurement'),
        ),
    ]
