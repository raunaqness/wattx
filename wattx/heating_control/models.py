from django.db import models
from enum import Enum

from django.db.models.expressions import F


class SensorType(Enum):
    Temperature = ('temperature', 'temperature')


class Room(models.Model):
    roomID = models.CharField(
        max_length=20,
        blank=False,
        null=False
    )
    motion_present = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
class Valve(models.Model):
    valveID = models.CharField(
        max_length=20,
        blank=False,
        null=False
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    level = models.IntegerField(
        blank=False,
        null=False,
        default=0
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    
class Sensor(models.Model):
    sensorID = models.CharField(
        max_length=20,
        blank=False,
        null=False
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    type = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        choices=[x.value for x in SensorType],
        default="temperature"
    )
    value = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.0
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    
