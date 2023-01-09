from rest_framework.viewsets import ModelViewSet

from .models import Appointment, Session
from .serializers import (
    AppointmentSerializer,
    SessionSerializer,
    UpdateAppointmentSerializer,
)


class SessionViewSet(ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class AppointmentViewSet(ModelViewSet):

    queryset = Appointment.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return UpdateAppointmentSerializer
        return AppointmentSerializer
