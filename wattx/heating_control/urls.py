from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from heating_control.views import *

urlpatterns = [
    path('sensors', SensorListView.as_view()),
    path('rooms', RoomListView.as_view()),
    path('valves', ValveListView.as_view()),
]