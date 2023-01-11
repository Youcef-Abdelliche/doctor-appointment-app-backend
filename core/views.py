from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, mixins

from .models import Doctor, Patient
from .permissions import IsDoctor
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
            permission_classes = [IsDoctor]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class PatientProfileView(RetrieveUpdateAPIView):

    queryset = Patient.objects.all()
    serializer_class = UpdatePatientSerializer

    def retrieve(self, request, *args, **kwargs):
        user_id = request.user.pk
        patient = get_object_or_404(Patient.objects.all(), user_id=user_id)
        serializer = self.get_serializer(patient)
        return Response(serializer.data)


class DoctorProfileView(RetrieveUpdateAPIView):

    queryset = Doctor.objects.all()
    serializer_class = UpdateDoctorSerializer

    def retrieve(self, request, *args, **kwargs):
        user_id = request.user.pk
        doctor = get_object_or_404(Doctor.objects.all(), user_id=user_id)
        serializer = self.get_serializer(doctor)
        return Response(serializer.data)
