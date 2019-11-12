from django.urls import path
from .views import simulator, views, dashboard

app_name = "mercury"
urlpatterns = [
    path("", views.HomePageView.as_view(), name="index"),
    path("about/", views.AboutPageView.as_view(), name="about"),
    path("simulator/", simulator.TemperatureView.as_view(), name="simulator"),
    path("dashboard/", dashboard.DashboardView.as_view(), name="dashboard"),
]
