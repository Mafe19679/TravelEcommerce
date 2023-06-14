from . import views
from django.shortcuts import render
from django.urls import path
from orders.views import UserListView
from django.urls import re_path
from .views import HotelCreateAPIView,VueloListApi, HotelListApi, ReservaVueloListApi, ReservaVueloCreateAPIView, ReservaHotelCreateAPIView

# from ecommerce.orders.views import UserListView
urlpatterns = [
    # vuelo
    # path("listView/", UserListView.as_view(), name="listView"),
    path("", views.home),
    path("activarServicios/", views.activarServicios),
    # http://127.0.0.1:3000/accounts/login/?next=/
    path('registrarVuelo/', views.registrarVuelo),
    path('activarServicios/edicionVuelo/<IDVuelo>', views.edicionVuelo),
    path('editarVuelo/', views.editarVuelo),
    path('activarServicios/eliminarVuelo/<IDVuelo>', views.eliminarVuelo),
    # hotel
    path('registrarHotel/', views.registrarHotel),
    path('activarServicios/edicionHotel/<IDHotel>', views.edicionHotel),
    path('editarHotel/', views.editarHotel),
    path('activarServicios/eliminarHotel/<IDHotel>', views.eliminarHotel),
    path('salir/', views.salir),
    # re_path(r"^createReservaVuelo$", HotelCreateAPIView.as_view(), name="createReservaVuelo"),
    path('reservas/', views.Reservas),
    # reserva vuelo
    path('registrarReservaVuelo/', views.registrarReservaVuelo),
    path('reservas/edicionReservaVuelo/<IDReservaVuelo>', views.edicionReservaVuelo),
    path('editarReservaVuelo/', views.editarReservaVuelo),
    path('eliminarReservaVuelo/<IDReservaVuelo>', views.eliminarReservaVuelo),
    path('registrarReservaHotel/', views.registrarReservaHotel),
    path('reservas/edicionReservaHotel/<IDReservaHotel>', views.edicionReservaHotel),
    path('editarReservaHotel/', views.editarReservaHotel),
    path('eliminarReservaHotel/<IDReservaHotel>', views.eliminarReservaHotel),

]

app_name = 'orders'

# urlpatterns = [
#     re_path(r"^getVuelo$", VueloListApi.as_view(), name="getVuelo"),
#     re_path(r"^getReservaVuelo$", ReservaVueloListApi.as_view(), name="getReservaVuelo"),
#     re_path(r"^getHotel$", HotelListApi.as_view(), name="getHotel"),
#     re_path(r"^createReservaVuelo$", ReservaVueloCreateAPIView.as_view(), name="createReservaVuelo"),
#     re_path(r"^createReservaHotel$", ReservaHotelCreateAPIView.as_view(), name="createReservaHotel"),

# ]


