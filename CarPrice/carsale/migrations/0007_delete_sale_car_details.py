# Generated by Django 3.2.7 on 2022-05-16 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carsale', '0006_buyer_booking_details'),
    ]

    operations = [
        migrations.DeleteModel(
            name='sale_car_details',
        ),
    ]
