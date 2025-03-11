from django.contrib import admin
from .models import Trip, RouteStop, Location, LogEntry, Driver

admin.site.register(Trip)
admin.site.register(RouteStop)
admin.site.register(Location)
admin.site.register(LogEntry)
admin.site.register(Driver)
