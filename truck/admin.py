from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Trip, Truck, VehicleModel


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    empty_value_display = _('-empty-')
    list_display = ('event_time', 'truck', 'weight')
    list_filter = ('event_time', 'truck')
    search_fields = ('event_time', 'truck')


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    empty_value_display = _('-empty-')
    list_display = ('model', 'side_number')
    list_filter = ('model',)
    search_fields = ('side_number',)

@admin.register(VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
    empty_value_display = _('-empty-')
    list_display = ('name', 'carrying')
    search_fields = ('name',)
