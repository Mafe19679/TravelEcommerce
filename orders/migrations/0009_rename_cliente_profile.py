# Generated by Django 4.2.1 on 2023-06-09 19:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0008_remove_cliente_contraseñacliente_cliente_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cliente',
            new_name='profile',
        ),
    ]
