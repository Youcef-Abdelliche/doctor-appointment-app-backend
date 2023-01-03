from rest_framework.viewsets import ModelViewSet

from .models import Doctor, User
from .serializers import (
    CreateUpdateDoctorSerializer,
    DoctorSerializer,
    UserDoctorRegistrationSerializer,
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
