from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Driver

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class DriverSerializer(serializers.ModelSerializer):
    user_info = UserSerializer(source='user', read_only=True)
    
    class Meta:
        model = Driver
        fields = ['id', 'user', 'user_info', 'license_number', 'phone_number', 'available_hours']

class DriverDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Driver
        fields = ['id', 'user', 'license_number', 'phone_number', 'available_hours']