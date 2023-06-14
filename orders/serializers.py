from .models import Cliente, Hotel, Vuelo, reservaHotel, reservaVuelo  

from rest_framework.serializers import ModelSerializer 
from rest_framework.serializers import (
    SerializerMethodField
)
from rest_framework import serializers

class VueloSerializer(ModelSerializer):
    
    class Meta:
        model = Vuelo
        fields = '__all__'

class ReservaVueloSerializer(ModelSerializer):
    IDVueloReservaVuelo=VueloSerializer(many=False)
    class Meta:
        model = reservaVuelo
        fields = '__all__' 

class ReservaVueloSerializer(ModelSerializer):
    IDVueloReservaVuelo=VueloSerializer(many=False)
    class Meta:
        model = reservaVuelo
        fields = '__all__' 

class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'  

class ReservaHotelSerializer(ModelSerializer):
    # IDVueloReservaVuelo=VueloSerializer(many=False)
    class Meta:
        model = reservaHotel
        fields = '__all__' 
    

      
