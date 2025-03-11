from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # لوحة تحكم Django
    path('api/', include('trips.urls')),  
]
