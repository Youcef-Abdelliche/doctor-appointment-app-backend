from rest_framework.viewsets import ModelViewSet

from .models import Appointment, Session
from .serializers import (
    AppointmentSerializer,
    SessionSerializer,
    UpdateAppointmentSerializer,
    UpdateSessionSerializer,
)


class SessionViewSet(ModelViewSet):
    queryset = Session.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return UpdateSessionSerializer
        return SessionSerializer


class AppointmentViewSet(ModelViewSet):

    queryset = Appointment.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return UpdateAppointmentSerializer
        return AppointmentSerializer


# class DoctorAppointmentViewSet(
#         mixins.ListModelMixin,
#         mixins.RetrieveModelMixin,
#         GenericAPIView):

#     serializer_class = AppointmentSerializer

#     def get_queryset(self):
#         return Appointment.objects.filter(
# session__doctor__user_id=self.request.user.pk).all()
