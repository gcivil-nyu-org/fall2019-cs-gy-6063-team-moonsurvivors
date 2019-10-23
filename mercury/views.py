from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .forms import VehicleForm
import datetime


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "index.html", context=None)


class AboutPageView(TemplateView):
    template_name = "about.html"


class SimulatorView(TemplateView):
    template_name = "simulator.html"
    form_class = VehicleForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/simulator/")
        return render(request, self.template_name, {"form": form})

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={"created_at": datetime.datetime.now()})
        return render(request, "simulator.html", {"form": form})


class DashboardView(TemplateView):
    template_name = "dashboard.html"
