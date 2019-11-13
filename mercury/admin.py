from django.contrib import admin  # noqa f401

# Register your models here.
from .models import TemperatureSensor, AccelerationSensor,WheelSpeedSensor

admin.site.register(TemperatureSensor)
admin.site.register(AccelerationSensor)
admin.site.register(WheelSpeedSensor)


