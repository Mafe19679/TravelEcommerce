# Generated by Django 4.2.1 on 2023-06-09 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_hotel_imagenhotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='imagenHotel',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]