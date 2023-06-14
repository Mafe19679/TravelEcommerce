from django.contrib import admin
from .models import Cliente, Hotel, Vuelo, reservaHotel, reservaVuelo  

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Hotel)
admin.site.register(reservaHotel)
admin.site.register(Vuelo)
admin.site.register(reservaVuelo)