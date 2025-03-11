from django.http.response import JsonResponse
from django.utils.timezone import now
from ..models.trip import Trip
def create_trip(request):
    return

def get_trips(request):
    data = Trip.objects.all()
    response = {
        'trips':list(data.values())
    }
    return JsonResponse(response)

