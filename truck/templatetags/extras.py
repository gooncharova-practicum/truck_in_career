from django import template

register = template.Library()

ONE_HUNDRED_PER = 100


@register.filter(name='truck_overload')
def truck_overload(weight, carrying):
    overload = ((weight-carrying)/carrying)*ONE_HUNDRED_PER
    if overload < 0:
        return 0
    return round(overload, 2)
