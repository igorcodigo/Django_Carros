# Generated by Django 5.0.3 on 2024-04-14 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_alter_car_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='creator',
        ),
    ]
