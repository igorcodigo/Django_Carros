# Generated by Django 4.2.6 on 2024-02-12 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_brand_alter_car_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='troll',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
