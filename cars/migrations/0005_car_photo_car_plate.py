# Generated by Django 4.2.6 on 2024-02-13 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_remove_brand_troll'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cars/'),
        ),
        migrations.AddField(
            model_name='car',
            name='plate',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
