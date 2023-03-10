# from django.urls import path
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()

router.register("sessions", views.SessionViewSet, basename="sessions")
router.register("appointments", views.AppointmentViewSet, basename="appointments")

urlpatterns = router.urls
