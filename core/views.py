from rest_framework.viewsets import ModelViewSet

from .models import Doctor, Patient, User
from .serializers import (
    CreateUpdateDoctorSerializer,
    CreateUpdatePatientSerializer,
    DoctorSerializer,
    PatientSerializer,
    UserDoctorRegistrationSerializer,
    UserPatientRegisrationSerializer,
)


class DoctorViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.request.method == "GET":
            return DoctorSerializer
        elif self.request.method == "POST":
            return UserDoctorRegistrationSerializer
        return CreateUpdateDoctorSerializer

    def get_queryset(self):
        if self.request.method == "GET":
            return Doctor.objects.all()
        return User.objects.filter(user_type=2).all()


class PatientViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserPatientRegisrationSerializer
        elif self.request.method == "GET":
            return PatientSerializer
        return CreateUpdatePatientSerializer

    def get_queryset(self):
        if self.request.method == "GET":
            return Patient.objects.all()
        return User.objects.filter(user_type=3).all()
