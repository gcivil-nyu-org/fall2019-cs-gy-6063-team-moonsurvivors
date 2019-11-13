from django.test import TestCase
from mercury.models import (
    TemperatureSensor,
    # AccelerationSensor,
    # WheelSpeedSensor,
    # SuspensionSensor,
    # FuelLevelSensor,
)
import datetime

TEST_TEMP = 999.0


# TODO
def create_simulated_temp():
    TemperatureSensor.objects.create(
        temperature=TEST_TEMP, created_at=datetime.datetime.now()
    )


class TestTemperatureSensor(TestCase):
    def setUp(self):
        create_simulated_temp()

    def test_vehicle_temp(self):
        foo = TemperatureSensor.objects.get(temperature=TEST_TEMP)
        self.assertEqual(foo.temperature, TEST_TEMP)

    def test_vehicle_temp_method(self):
        foo = TemperatureSensor()
        foo.temperature = 987
        self.assertEqual(foo.temp(), 987)
