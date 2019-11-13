from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from mercury.models import (
    TemperatureSensor,
    AccelerationSensor,
    WheelSpeedSensor,
    SuspensionSensor,
    FuelLevelSensor,
)

# TODO check with Dave,


class TemperatureSensorResource(ModelResource):
    """This class exposes an API for the TemperatureData object with the resource name
    defined below as the 'resource_name'."""

    class Meta:
        queryset = TemperatureSensor.objects.all()
        resource_name = "tempsensor"
        authorization = Authorization()


class AccelerationSensorResource(ModelResource):
    """This class exposes an API for the AccelerationSensor object with the resource name
    defined below as the 'resource_name'."""

    class Meta:
        queryset = AccelerationSensor.objects.all()
        resource_name = "accel_sensor"
        authorization = Authorization()


class WheelSpeedSensorResource(ModelResource):
    """This class exposes an API for the WheelSpeedSensor object with the resource name
    defined below as the 'resource_name'."""

    class Meta:
        queryset = WheelSpeedSensor.objects.all()
        resource_name = "wheel_speed_sensor"
        authorization = Authorization()


class SuspensionSensorResource(ModelResource):
    """This class exposes an API for the SuspensionSensor object with the resource name
    defined below as the 'resource_name'."""

    class Meta:
        queryset = SuspensionSensor.objects.all()
        resource_name = "suspension_sensor"
        authorization = Authorization()


class FuelLevelSensorResource(ModelResource):
    """This class exposes an API for the FuelLevelSensor object with the resource name
    defined below as the 'resource_name'."""

    class Meta:
        queryset = FuelLevelSensor.objects.all()
        resource_name = "fuel_level_sensor"
        authorization = Authorization()
