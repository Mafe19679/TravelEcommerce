from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
   
    cedulaCliente = models.IntegerField(primary_key=True)
    nombreCliente = models.CharField(max_length=100)
    telefonoCliente = models.IntegerField()
    correoCliente = models.EmailField(max_length=100)
    direccionCliente = models.CharField(max_length=300)
    contraseñaCliente = models.CharField('Contraseña', max_length=30)
    
   
    def __str__(self):
        return f'{self.cedulaCliente}'
       
class Hotel(models.Model):
    IDHotel = models.BigAutoField(primary_key=True)
    nombreHotel = models.CharField(max_length=100)
    estrellasHotel = models.IntegerField()
    costoHotel = models.IntegerField()
    serviciosHotel = models.CharField(max_length=500)
    imagenHotel = models.ImageField(upload_to='images/', blank=True, null=True)
    
    def __str__(self):
        return f'{self.IDHotel}'

class reservaHotel(models.Model):
    IDReservaHotel = models.BigAutoField(primary_key=True)
    cedulaClienteReservaHotel = models.ForeignKey(Cliente , on_delete=models.CASCADE , null=True)
    IDHotelReservaHotel = models.ForeignKey(Hotel , on_delete=models.CASCADE , null=True)
    cantidadPersonasReservaHotel = models.IntegerField()
    cantidadHabitacionesReservaHotel = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.IDReservaHotel}'
    
class Vuelo(models.Model):
    IDVuelo = models.BigAutoField(primary_key=True)
    origenVuelo = models.CharField(max_length=100)
    destinoVuelo = models.CharField(max_length=100)
    fechaVuelo = models.DateField()
    horaSalidaVuelo = models.TimeField()
    horaLlegadaVuelo = models.TimeField()
    sillasDisponibleVuelo = models.IntegerField()
    costoVuelo = models.IntegerField()
    
    def __str__(self):
        return f'{self.IDVuelo}'
    
class reservaVuelo(models.Model):
    IDReservaVuelo = models.BigAutoField(primary_key=True)
    cedulaClienteReservaVuelo = models.ForeignKey(Cliente , on_delete=models.CASCADE , null=True)
    cantidadPersonasReservaVuelo = models.IntegerField()
    IDVueloReservaVuelo = models.ForeignKey(Vuelo , on_delete=models.CASCADE , null=True)

    def __str__(self):
        return f'{self.IDReservaVuelo}'
    
    
