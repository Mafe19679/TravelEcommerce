# Generated by Django 4.2.1 on 2023-06-01 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_cliente_hotel_reservahotel_reservavuelo_vuelo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='costoHotel',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='nombreHotel',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='serviciosHotel',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='reservahotel',
            name='cantidadHabitacionesReservaHotel',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='destinoVuelo',
            field=models.CharField(max_length=100),
        ),
    ]
