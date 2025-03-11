from django.db import models
from .trip import Trip
from .location import Location
from ..Enums.stop_type import StopType

class RouteStop(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='stops')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    stop_type = models.CharField(max_length=20, choices=StopType.CHOICES)
    planned_arrival = models.DateTimeField()
    planned_departure = models.DateTimeField()
    actual_arrival = models.DateTimeField(null=True, blank=True)
    actual_departure = models.DateTimeField(null=True, blank=True)
    distance_from_last_stop = models.FloatField(default=0)  # المسافة بين كل توقف

    def __str__(self):
        return f"{self.get_stop_type_display()} at {self.location.name}"
