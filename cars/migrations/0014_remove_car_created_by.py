# Generated by Django 5.0.3 on 2024-04-14 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0013_alter_car_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='created_by',
        ),
    ]