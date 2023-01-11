from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser as IsStaffUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.permissions import IsDoctor

from .models import Appointment, Session
from .serializers import (
    AppointmentSerializer,
    SessionAppointmentSerializer,
    SessionSerializer,
    UpdateAppointmentSerializer,
    UpdateSessionSerializer,
)


class SessionViewSet(ModelViewSet):
    queryset = Session.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return UpdateSessionSerializer
        elif self.action in ["my_sessions"]:
            return SessionAppointmentSerializer
        return SessionSerializer

    @action(["get"], detail=False)
    def my_sessions(self, request):
        user_id = request.user.pk
        my_sessions = Session.objects.filter(doctor_id=user_id).all()
        serializer = self.get_serializer(my_sessions, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action in ["my_sessions"]:
            permission_classes = [IsDoctor]
        elif self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            permission_classes = [IsStaffUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class AppointmentViewSet(ModelViewSet):

    http_method_names = ["post", "get", "delete"]
    queryset = Appointment.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return UpdateAppointmentSerializer
        return AppointmentSerializer

    def get_serializer_context(self):
        if self.action == "create":
            return {"user_id": self.request.user.pk}
        return super().get_serializer_context()

    def get_permissions(self):
        if self.action in ["all_appointments"]:
            permission_classes = [IsDoctor]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        user_id = request.user.pk
        appointments = Appointment.objects.filter(patient_id=user_id).all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        user_id = request.user.pk
        appointment = get_object_or_404(
            Appointment.objects.all(), patient_id=user_id, id=kwargs["pk"]
        )
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        user_id = request.user.pk
        appointment = get_object_or_404(
            Appointment.objects.all(), patient_id=user_id, id=kwargs["pk"]
        )
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(["get"], detail=False)
    def all_appointments(self, request):
        user_id = request.user.pk
        my_appointments = Appointment.objects.filter(session__doctor_id=user_id).all()
        serializer = self.get_serializer(my_appointments, many=True)
        return Response(serializer.data)
