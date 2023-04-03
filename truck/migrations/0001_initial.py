# Generated by Django 4.1.4 on 2023-04-02 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('carrying', models.PositiveIntegerField(verbose_name='Грузоподъемность, т')),
            ],
            options={
                'verbose_name': 'модель транспортного средства',
                'verbose_name_plural': 'модели транспортных средств',
            },
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side_number', models.CharField(max_length=50, verbose_name='Бортовой номер')),
                ('model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='truck', to='truck.vehiclemodel', verbose_name='Модель самосвала')),
            ],
            options={
                'verbose_name': 'самосвал',
                'verbose_name_plural': 'самосвалы',
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveIntegerField(verbose_name='Масса руды, т')),
                ('event_time', models.DateTimeField(verbose_name='Время события')),
                ('truck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip', to='truck.truck', verbose_name='Самосвал')),
            ],
            options={
                'verbose_name': 'рейс с рудой',
                'verbose_name_plural': 'рейсы с рудой',
            },
        ),
    ]
