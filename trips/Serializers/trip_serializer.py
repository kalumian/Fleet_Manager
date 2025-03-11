from rest_framework import serializers
from ..models import Trip
from .driver_serializer import DriverSerializer
from .location_serializer import LocationSerializer

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = [
            'id', 'driver', 'current_location', 'pickup_location', 
            'dropoff_location', 'status', 'created_at', 'started_at', 
            'completed_at', 'current_cycle_hours_used', 'estimated_distance', 
            'estimated_duration'
        ]

class TripCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = [
            'driver', 'current_location', 'pickup_location', 
            'dropoff_location', 'current_cycle_hours_used'
        ]
    
    def create(self, validated_data):
        # Here you could add custom logic for creating a trip
        # For example, calculating estimated_distance and estimated_duration
        trip = Trip.objects.create(**validated_data)
        return trip

class TripDetailSerializer(serializers.ModelSerializer):
    driver = DriverSerializer(read_only=True)
    current_location = LocationSerializer(read_only=True)
    pickup_location = LocationSerializer(read_only=True)
    dropoff_location = LocationSerializer(read_only=True)
    stops = serializers.SerializerMethodField()
    log_entries = serializers.SerializerMethodField()
    
    class Meta:
        model = Trip
        fields = [
            'id', 'driver', 'current_location', 'pickup_location', 
            'dropoff_location', 'status', 'created_at', 'started_at', 
            'completed_at', 'current_cycle_hours_used', 'estimated_distance', 
            'estimated_duration', 'stops', 'log_entries'
        ]
    
    def get_stops(self, obj):
        from .route_stop_serializer import RouteStopSerializer
        return RouteStopSerializer(obj.stops.all(), many=True).data
    
    def get_log_entries(self, obj):
        from .log_entry_serializer import LogEntrySerializer
        return LogEntrySerializer(obj.log_entries.all(), many=True).data