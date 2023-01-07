from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import GenericViewSet, mixins

from .models import Doctor, Patient
from .serializers import (
    DoctorSerializer,
    PatientSerializer,
    UpdateDoctorSerializer,
    UpdatePatientSerializer,
)


class DoctorViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):

    queryset = Doctor.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return UpdateDoctorSerializer
        return DoctorSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class PatientViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):

    queryset = Patient.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return UpdatePatientSerializer
        return PatientSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
