# Generated by Django 4.2.1 on 2023-06-02 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_reservahotel_idhotelreservahotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='imagenHotel',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]