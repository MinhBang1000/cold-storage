# Generated by Django 4.1 on 2022-11-06 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='sensor_code',
            field=models.IntegerField(default=0),
        ),
    ]
