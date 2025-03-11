from django.urls import path
from trips.views import create_trip, get_trips
from trips.views import user_login, user_logout
urlpatterns = [
    path('trips/', get_trips, name='get_trips'),
    path('trips/create/', create_trip, name='create_trip'),
    path('auth/login/', user_login, name='user_login'),
    path('auth/logout/', user_logout, name='user_logout'),
]
