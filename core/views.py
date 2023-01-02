from rest_framework.viewsets import ModelViewSet

from .models import Doctor
from .serializers import CreateUpdateDoctorSerializer, DoctorSerializer


class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DoctorSerializer
        return CreateUpdateDoctorSerializer
