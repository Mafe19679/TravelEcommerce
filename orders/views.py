from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from core.users.models import Profile, User
from django.views.generic import ListView
from django.urls import reverse_lazy
from requests import request
from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView)    # GenericAPIView
from .models import Cliente, Hotel, Vuelo, reservaHotel, reservaVuelo  
from django.contrib import messages


from .serializers import VueloSerializer, HotelSerializer, ReservaVueloSerializer, ReservaHotelSerializer
# Create your views here.
# redirect('base.html')
@login_required
def index(request):
    return render(request, 'plantilla/base.html/')

def salir(request):
    logout(request)
    return redirect('/')

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'object_list'
    paginate_by = 10 # usuarios por pagina
    queryset = User.objects.all() #consulta para obtener lista de usuarios
    ordering = ['username']

# @permission_classes((AllowAny, ))
class VueloListApi(ListAPIView):
    serializer_class = VueloSerializer
    queryset = Vuelo.objects.all().order_by('fechaVuelo'),

class ReservaVueloListApi(ListAPIView):
    serializer_class = ReservaVueloSerializer
    queryset = reservaVuelo.objects.all()
 
class HotelListApi(ListAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

class HotelCreateAPIView(CreateAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

class ReservaVueloCreateAPIView(CreateAPIView):
    queryset = reservaVuelo.objects.all()
    serializer_class = ReservaVueloSerializer

class ReservaHotelCreateAPIView(CreateAPIView):
    queryset = reservaHotel.objects.all()
    serializer_class = ReservaHotelSerializer

def home(request):
    return render(request, "base.html")


def activarServicios(request):
    vuelosListados = Vuelo.objects.all()
    hotelesListados = Hotel.objects.all()
    # messages.success(request, '¡Vuelos listados!')
    return render(request, "servicios_create_list.html", {"vuelos": vuelosListados, "hoteles": hotelesListados})

def registrarVuelo(request):
    # IDVuelo = request.POST['txtIDVuelo']
    origenVuelo = request.POST['txtorigenVuelo']
    destinoVuelo = request.POST['destinoVuelo']
    fechaVuelo = request.POST['fechaVuelo']
    horaSalidaVuelo = request.POST['horaSalidaVuelo']
    horaLlegadaVuelo = request.POST['horaLlegadaVuelo']
    sillasDisponibleVuelo = request.POST['sillasDisponibleVuelo']
    costoVuelo = request.POST['costoVuelo']

    vuelo = Vuelo.objects.create(
        origenVuelo=origenVuelo, destinoVuelo=destinoVuelo, fechaVuelo=fechaVuelo, horaSalidaVuelo=horaSalidaVuelo, horaLlegadaVuelo=horaLlegadaVuelo,sillasDisponibleVuelo=sillasDisponibleVuelo, costoVuelo=costoVuelo)
    messages.success(request, '¡Vuelo registrado!')
    return redirect('/activarServicios/')


def edicionVuelo(request, IDVuelo):
    vuelo = Vuelo.objects.get(IDVuelo=IDVuelo)
    return render(request, "edicionVuelo.html", {"vuelo": vuelo})


def editarVuelo(request):
    IDVuelo = request.POST['txtIDVuelo']
    origenVuelo = request.POST['txtorigenVuelo']
    destinoVuelo = request.POST['destinoVuelo']
    fechaVuelo = request.POST['fechaVuelo']
    horaSalidaVuelo = request.POST['horaSalidaVuelo']
    horaLlegadaVuelo = request.POST['horaLlegadaVuelo']
    sillasDisponibleVuelo = request.POST['sillasDisponibleVuelo']
    costoVuelo = request.POST['costoVuelo']

    vuelo = Vuelo.objects.get(IDVuelo=IDVuelo)
    vuelo.origenVuelo = origenVuelo
    vuelo.destinoVuelo = destinoVuelo
    vuelo.fechaVuelo = fechaVuelo
    vuelo.horaSalidaVuelo = horaSalidaVuelo
    vuelo.horaLlegadaVuelo = horaLlegadaVuelo
    vuelo.sillasDisponibleVuelo = sillasDisponibleVuelo
    vuelo.costoVuelo = costoVuelo
    vuelo.save()
    

    messages.success(request, '¡Vuelo actualizado!')

    return redirect('/activarServicios/')



def eliminarVuelo(request, IDVuelo):
    vuelo = Vuelo.objects.get(IDVuelo=IDVuelo)
    vuelo.delete()

    messages.success(request, '¡Vuelo eliminado!')

    return redirect('/activarServicios/')

def registrarHotel(request):
    # IDHotel = request.POST['txtIDHotel']
    nombreHotel = request.POST['txtnombreHotel']
    estrellasHotel = request.POST['estrellasHotel']
    costoHotel = request.POST['costoHotel']
    serviciosHotel = request.POST['serviciosHotel']
    try:
        imagenHotel = request.FILES['imagenHotel']
    except:
        imagenHotel = "images/sinimagen.jpg"

    hotel = Hotel.objects.create(
        nombreHotel=nombreHotel, estrellasHotel=estrellasHotel, costoHotel=costoHotel, serviciosHotel=serviciosHotel, imagenHotel=imagenHotel)
    messages.success(request, '¡Hotel registrado!')

    return redirect('/activarServicios/')


def edicionHotel(request, IDHotel):
    hotel = Hotel.objects.get(IDHotel=IDHotel)
    return render(request, "edicionHotel.html", {"hotel": hotel})


def editarHotel(request):
    IDHotel = request.POST['txtIDHotel']
    nombreHotel = request.POST['txtnombreHotel']
    estrellasHotel = request.POST['estrellasHotel']
    costoHotel = request.POST['costoHotel']
    serviciosHotel = request.POST['serviciosHotel']
    # imagenHotel = request.FILES['imagenHotel']

    try:
        imagenHotel = request.FILES['imagenHotel']
        hotel = Hotel.objects.get(IDHotel=IDHotel)
        hotel.imagenHotel = imagenHotel
        hotel.save()
    except:
        imagenHotel = "images/sinimagen.jpg"

    hotel = Hotel.objects.get(IDHotel=IDHotel)
    hotel.nombreHotel = nombreHotel
    hotel.estrellasHotel = estrellasHotel
    hotel.costoHotel = costoHotel
    hotel.serviciosHotel = serviciosHotel
    hotel.save()

    messages.success(request, '¡Hotel actualizado!')

    return redirect('/activarServicios/')


def eliminarHotel(request, IDHotel):
    hotel = Hotel.objects.get(IDHotel=IDHotel)
    hotel.delete()
    
    messages.success(request, '¡Hotel eliminado!')

    return redirect('/activarServicios/')


# Reservas ---------------------------------------------------------------

def Reservas(request):
    ReservaVueloListados = reservaVuelo.objects.all()
    ReservaHotelListados = reservaHotel.objects.all()
    # messages.success(request, '¡Vuelos listados!')
    return render(request, "reservas_create_list.html", {"reservaVuelo": ReservaVueloListados, "reservaHotel": ReservaHotelListados})


def registrarReservaVuelo(request):
    # IDReservaVuelo = request.POST['IDReservaVuelo']
    cedulaClienteReservaVuelo = Cliente.objects.get(cedulaCliente = request.POST['cedulaClienteReservaVuelo'])
    cantidadPersonasReservaVuelo = request.POST['cantidadPersonasReservaVuelo']
    IDVueloReservaVuelo = Vuelo.objects.get(IDVuelo = request.POST['IDVueloReservaVuelo'])

    # IDVueloReservaVuelo = request.POST['IDVueloReservaVuelo']
    
    ReservaVuelo = reservaVuelo.objects.create(
       cedulaClienteReservaVuelo=cedulaClienteReservaVuelo, 
       cantidadPersonasReservaVuelo=cantidadPersonasReservaVuelo, IDVueloReservaVuelo=IDVueloReservaVuelo)
    messages.success(request, '¡Vuelo registrado!')
    return redirect('/reservas/')


def edicionReservaVuelo(request, IDReservaVuelo):
    ReservaVuelo = reservaVuelo.objects.get(IDReservaVuelo=IDReservaVuelo)
    return render(request, "edicionReservaVuelo.html", {"reservaVuelo": ReservaVuelo})


def editarReservaVuelo(request):
    IDReservaVuelo = request.POST['IDReservaVuelo']
    cedulaClienteReservaVuelo = Cliente.objects.get(cedulaCliente = request.POST['cedulaClienteReservaVuelo'])
    cantidadPersonasReservaVuelo = request.POST['cantidadPersonasReservaVuelo']
    IDVueloReservaVuelo = Vuelo.objects.get(IDVuelo = request.POST['IDVueloReservaVuelo'])
   
    ReservaVuelo = reservaVuelo.objects.get(IDReservaVuelo=IDReservaVuelo)
    ReservaVuelo.cedulaClienteReservaVuelo = cedulaClienteReservaVuelo
    ReservaVuelo.cantidadPersonasReservaVuelo = cantidadPersonasReservaVuelo
    ReservaVuelo.IDVueloReservaVuelo = IDVueloReservaVuelo
    ReservaVuelo.save()
    
    messages.success(request, '¡Reserva Vuelo actualizado!')

    return redirect('/reservas/')



def eliminarReservaVuelo(request, IDReservaVuelo):
    ReservaVuelo = reservaVuelo.objects.get(IDReservaVuelo=IDReservaVuelo)
    ReservaVuelo.delete()

    messages.success(request, '¡Reserva Vuelo eliminado!')

    return redirect('/reservas/')


def registrarReservaHotel(request):
    # IDReservaHotel = request.POST['IDReservaHotel']
    cedulaClienteReservaHotel = Cliente.objects.get(cedulaCliente = request.POST['cedulaClienteReservaHotel'])
    IDHotelReservaHotel = Hotel.objects.get(IDHotel = request.POST['IDHotelReservaHotel'])
    cantidadPersonasReservaHotel = request.POST['cantidadPersonasReservaHotel']
    cantidadHabitacionesReservaHotel = request.POST['cantidadHabitacionesReservaHotel']
   

    ReservaHotel = reservaHotel.objects.create(
        cedulaClienteReservaHotel=cedulaClienteReservaHotel, IDHotelReservaHotel=IDHotelReservaHotel, cantidadPersonasReservaHotel=cantidadPersonasReservaHotel, cantidadHabitacionesReservaHotel=cantidadHabitacionesReservaHotel)
    messages.success(request, '¡Hotel registrado!')
    return redirect('/reservas/')


def edicionReservaHotel(request, IDReservaHotel):
    ReservaHotel = reservaHotel.objects.get(IDReservaHotel=IDReservaHotel)
    return render(request, "edicionReservaHotel.html", {"reservaHotel": ReservaHotel})


def editarReservaHotel(request):
    IDReservaHotel = request.POST['IDReservaHotel']
    cedulaClienteReservaHotel = Cliente.objects.get(cedulaCliente = request.POST['cedulaClienteReservaHotel'])
    IDHotelReservaHotel = Hotel.objects.get(IDHotel = request.POST['IDHotelReservaHotel'])
    cantidadPersonasReservaHotel = request.POST['cantidadPersonasReservaHotel']
    cantidadHabitacionesReservaHotel = request.POST['cantidadHabitacionesReservaHotel']
   
    ReservaHotel = reservaHotel.objects.get(IDReservaHotel=IDReservaHotel)
    ReservaHotel.cedulaClienteReservaHotel = cedulaClienteReservaHotel
    ReservaHotel.IDHotelReservaHotel = IDHotelReservaHotel
    ReservaHotel.cantidadPersonasReservaHotel = cantidadPersonasReservaHotel
    ReservaHotel.cantidadHabitacionesReservaHotel = cantidadHabitacionesReservaHotel
    ReservaHotel.save()
    
    messages.success(request, '¡Reserva Hotel actualizado!')

    return redirect('/reservas/')



def eliminarReservaHotel(request, IDReservaHotel):
    ReservaHotel = reservaHotel.objects.get(IDReservaHotel=IDReservaHotel)
    ReservaHotel.delete()

    messages.success(request, '¡Reserva Hotel eliminado!')

    return redirect('/reservas/')
