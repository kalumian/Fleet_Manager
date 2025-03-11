from rest_framework import serializers
from ..models import RouteStop
from .location_serializer import LocationSerializer

class RouteStopSerializer(serializers.ModelSerializer):
    location_details = LocationSerializer(source='location', read_only=True)
    
    class Meta:
        model = RouteStop
        fields = [
            'id', 'trip', 'location', 'location_details', 'stop_type', 
            'planned_arrival', 'planned_departure', 'actual_arrival', 
            'actual_departure'
        ]