from rest_framework import serializers
from ..models import LogEntry
from .driver_serializer import DriverSerializer

class LogEntrySerializer(serializers.ModelSerializer):
    driver_details = DriverSerializer(source='driver', read_only=True)
    
    class Meta:
        model = LogEntry
        fields = [
            'id', 'trip', 'driver', 'driver_details', 'status', 
            'start_time', 'end_time', 'location'
        ]