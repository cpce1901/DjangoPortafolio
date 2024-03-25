from django.shortcuts import render
from .models import Sensor

def SensorsByPlace(request):
    template = 'htmx/sensorSelect.html'
    locate_id = request.GET.get('place')
    
    sensors_by_place = Sensor.objects.filter(place_id=locate_id)
    context = {
        'sensors': sensors_by_place
    }    
    return render(request, template, context)