from django.contrib import admin  # noqa f401

# Register your models here.
from .models import TemperatureSensor

admin.site.register(TemperatureSensor)
