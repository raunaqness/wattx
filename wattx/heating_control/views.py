from django.shortcuts import render
from django.views.generic import ListView

from heating_control.models import Sensor, Room, Valve
# Create your views here.

class SensorListView(ListView):
    queryset = Sensor.objects.order_by('-created_at')
    template_name = "heating_control/sensor_list.html"

class RoomListView(ListView):
    queryset = Room.objects.order_by('-created_at')
    template_name = "heating_control/room_list.html"

class ValveListView(ListView):
    queryset = Valve.objects.order_by('-created_at')
    template_name = "heating_control/valve_list.html"