from django.db import models

class Trip(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    current_location = models.CharField(max_length=255)   
    pickup_location = models.CharField(max_length=255)  
    dropoff_location = models.CharField(max_length=255)  
    current_cycle_hours = models.FloatField()   
    hours_driven_today = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ongoing') 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"Trip from {self.pickup_location} to {self.dropoff_location} ({self.status})"
