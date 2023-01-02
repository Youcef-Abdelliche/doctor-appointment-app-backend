from rest_framework import serializers

from .models import Doctor, Specialization, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "sex", "first_name", "last_name"]


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ["name"]


class DoctorSerializer(serializers.ModelSerializer):
    specialization = SpecializationSerializer(read_only=True)
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = ["id", "user", "specialization", "address"]
        read_only_fields = ("specialization",)


class CreateUpdateDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["id", "user", "specialization", "address"]
