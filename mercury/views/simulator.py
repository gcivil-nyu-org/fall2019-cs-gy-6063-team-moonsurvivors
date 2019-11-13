from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

from ..forms import TemperatureForm, AccelerationForm
from mercury.models import TemperatureSensor, AccelerationSensor, WheelSpeedSensor
import datetime

class SimulatorView(TemplateView):
    template_name = "simulator.html"

    def post(self, request, *args, **kwargs):
        """Used by AJAX method in the simulator.js file to save data
        from the simulator UI."""

        if request.POST.get("acceleration_x"):
            post_created_at_accel = request.POST.get("created_at_accel")
            post_acceleration_x = request.POST.get("acceleration_x")
            post_acceleration_y = request.POST.get("acceleration_y")
            post_acceleration_z = request.POST.get("acceleration_z")

            accel_data = AccelerationSensor(
                created_at_accel=post_created_at_accel,
                acceleration_x=post_acceleration_x,
                acceleration_y=post_acceleration_y,
                acceleration_z=post_acceleration_z,
            )
            accel_data.save()

        elif request.POST.get("created_at_ws"):

            post_created_at_ws = request.POST.get("created_at_ws")
            post_wheel_speed_fr = request.POST.get("wheel_speed_fr")
            post_wheel_speed_fl = request.POST.get("wheel_speed_fl")
            post_wheel_speed_br = request.POST.get("wheel_speed_br")
            post_wheel_speed_bl = request.POST.get("wheel_speed_bl")

            ws_data = WheelSpeedSensor(
                created_at_ws=post_created_at_ws,
                wheel_speed_fr=post_wheel_speed_fr,
                wheel_speed_fl=post_wheel_speed_fl,
                wheel_speed_br=post_wheel_speed_br,
                wheel_speed_bl=post_wheel_speed_bl,
            )
            ws_data.save()


        else:
            post_created_at = request.POST.get("created_at")
            post_temperature = request.POST.get("temperature")

            temp_data = TemperatureSensor(
                created_at=post_created_at,
                temperature=post_temperature,
            )
            temp_data.save()



        return HttpResponse(status=201)

    def get(self, request, *args, **kwargs):
        """This method will render the Simulator form when GET is used"""
        form = TemperatureForm(initial={"created_at": datetime.datetime.now()})
        form_accel = AccelerationForm(initial={"created_at_accel": datetime.datetime.now()})


        return render(request, self.template_name, {"form_accel": form_accel, "form":form})


# class SimulatorView(TemplateView):
#     template_name = "simulator.html"
#
#     def post(self, request, *args, **kwargs):
#         """Used by AJAX method in the simulator.js file to save data
#         from the simulator UI."""
#         post_created_at = request.POST.get("created_at")
#         post_temperature = request.POST.get("temperature")
#         post_acceleration_x = request.POST.get("acceleration_x")
#         post_acceleration_y = request.POST.get("acceleration_y")
#         post_acceleration_z = request.POST.get("acceleration_z")
#         post_wheel_speed_fr = request.POST.get("wheel_speed_fr")
#         post_wheel_speed_fl = request.POST.get("wheel_speed_fl")
#         post_wheel_speed_br = request.POST.get("wheel_speed_br")
#         post_wheel_speed_bl = request.POST.get("wheel_speed_bl")
#         post_suspension_fr = request.POST.get("suspension_fr")
#         post_suspension_fl = request.POST.get("suspension_fl")
#         post_suspension_br = request.POST.get("suspension_br")
#         post_suspension_bl = request.POST.get("suspension_bl")
#         post_current_fuel_level = request.POST.get("current_fuel_level")
#         sim_data = SimulatedData(
#             created_at=post_created_at,
#             temperature=post_temperature,
#             acceleration_x=post_acceleration_x,
#             acceleration_y=post_acceleration_y,
#             acceleration_z=post_acceleration_z,
#             wheel_speed_fr=post_wheel_speed_fr,
#             wheel_speed_fl=post_wheel_speed_fl,
#             wheel_speed_br=post_wheel_speed_br,
#             wheel_speed_bl=post_wheel_speed_bl,
#             suspension_fr=post_suspension_fr,
#             suspension_fl=post_suspension_fl,
#             suspension_br=post_suspension_br,
#             suspension_bl=post_suspension_bl,
#             current_fuel_level=post_current_fuel_level,
#         )
#         sim_data.save()
#         return HttpResponse(status=201)
#
#     def get(self, request, *args, **kwargs):
#         """This method will render the Simulator form when GET is used"""
#         form = SimulatorForm(initial={"created_at": datetime.datetime.now()})
#         return render(request, self.template_name, {"form": form})
