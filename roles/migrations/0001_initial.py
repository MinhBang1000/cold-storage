# Generated by Django 4.1 on 2022-10-30 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('permissions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=250)),
                ('role_creater', models.IntegerField(default=0)),
                ('role_permissions', models.ManyToManyField(blank=True, to='permissions.permission')),
            ],
        ),
    ]
