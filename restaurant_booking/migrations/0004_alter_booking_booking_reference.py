# Generated by Django 3.2.9 on 2021-11-27 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_booking', '0003_auto_20211127_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_reference',
            field=models.TextField(max_length=200, unique=True),
        ),
    ]
