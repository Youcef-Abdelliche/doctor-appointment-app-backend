from django.urls import path
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()

router.register("doctors", views.DoctorViewSet, basename="doctors")
router.register("patients", views.PatientViewSet, basename="patients")

urlpatterns = [
    path("patients/me/", views.PatientProfileView.as_view(), name="patients_me"),
    path("doctors/me/", views.DoctorProfileView.as_view(), name="doctors_me"),
] + router.urls
