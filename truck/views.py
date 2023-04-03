from django.db.models import Max
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from truck_in_career.settings import OPTION_VALUE_FOR_ALL_MODELS

from .models import Trip, VehicleModel


@csrf_exempt
def index(request):
    """ Главная страница """
    last_trips = {}
    models = VehicleModel.objects.all()
    if request.method == "POST":
        last_events_time = Trip.objects.values('truck').annotate(max_time=Max('event_time'))
        filters = {'event_time__in': [time['max_time'] for time in last_events_time]}
        model = request.POST['model']
        if model != OPTION_VALUE_FOR_ALL_MODELS:
            filters.update({'truck__model__name': model})
        last_trips = Trip.objects.select_related('truck', 'truck__model').filter(**filters)
    
    context = {'last_trips': last_trips, 'models': models, 'all_models': OPTION_VALUE_FOR_ALL_MODELS}
    return render(request, 'index.html', context)
