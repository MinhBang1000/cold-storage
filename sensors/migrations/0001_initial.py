# Generated by Django 4.1 on 2022-10-30 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('storages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_x', models.IntegerField()),
                ('sensor_y', models.IntegerField()),
                ('sensor_z', models.IntegerField()),
                ('sensor_temperature', models.FloatField()),
                ('sensor_category', models.CharField(default='001', max_length=3)),
                ('sensor_storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensors', to='storages.storage')),
            ],
        ),
    ]
