# Generated by Django 4.2.6 on 2024-02-12 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_brand_troll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='troll',
        ),
    ]
