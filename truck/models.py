from django.db import models
from django.utils.translation import gettext_lazy as _


class VehicleModel(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Наименование'))
    carrying = models.PositiveIntegerField(verbose_name=_('Грузоподъемность, т'))

    class Meta:
        verbose_name = _('модель транспортного средства')
        verbose_name_plural = _('модели транспортных средств')

    def __str__(self):
        return self.name


class Truck(models.Model):
    side_number = models.CharField(max_length=50, verbose_name=_('Бортовой номер'))
    model = models.ForeignKey(VehicleModel, on_delete=models.SET_NULL,
                              null=True, blank=True,
                              related_name='truck',
                              verbose_name=_('Модель самосвала'))

    class Meta:
        verbose_name = _('самосвал')
        verbose_name_plural = _('самосвалы')

    def __str__(self):
        return self.side_number


class Trip(models.Model):
    weight = models.PositiveIntegerField(verbose_name=_('Масса руды, т'))
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE,
                              related_name='trip',
                              verbose_name=_('Самосвал'))
    event_time = models.DateTimeField(verbose_name=_('Время события'))

    class Meta:
        verbose_name = _('рейс с рудой')
        verbose_name_plural = _('рейсы с рудой')

    def __str__(self):
        return (f'{self.truck} на момент {self.event_time} '
                   'перевозил {self.weight} т руды')
