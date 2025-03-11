from django.db import models
from .driver import Driver
from .location import Location
from ..Enums.trip_status import TripStatus

class Trip(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='trips_current')
    pickup_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='trips_pickup')
    dropoff_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='trips_dropoff')
    status = models.CharField(max_length=20, choices=TripStatus.CHOICES, default=TripStatus.PLANNED)
    created_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    current_cycle_hours_used = models.FloatField(default=0)
    estimated_distance = models.FloatField(default=0) 
    estimated_duration = models.FloatField(default=0) 


    actual_distance = models.FloatField(null=True, blank=True)  
    actual_duration = models.FloatField(null=True, blank=True)  

    def __str__(self):
        return f"Trip {self.id}: {self.pickup_location.name} to {self.dropoff_location.name}"
