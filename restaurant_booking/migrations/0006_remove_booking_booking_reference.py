# Generated by Django 3.2.9 on 2021-11-27 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_booking', '0005_alter_booking_booking_reference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_reference',
        ),
    ]
