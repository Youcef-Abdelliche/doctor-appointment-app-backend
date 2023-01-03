from django.db import transaction
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from .models import Doctor, Specialization, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "sex", "first_name", "last_name"]


class CreateUpdateDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["specialization", "address"]


class UserRegistrationSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "sex", "first_name", "last_name", "user_type"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            user.is_active = True
            user.save(update_fields=["is_active"])
        return user


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ["name"]


class UserDoctorRegistrationSerializer(serializers.ModelSerializer):
    doctor = CreateUpdateDoctorSerializer()

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "sex",
            "first_name",
            "last_name",
            "user_type",
            "doctor",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "user_type": {"read_only": True},
        }

    def create(self, validated_data):
        with transaction.atomic():
            validated_data["user_type"] = 2
            print(validated_data)
            doctor = validated_data.pop("doctor")
            user = User.objects.create_user(**validated_data)
            Doctor.objects.create(
                user=user,
                address=doctor["address"],
                specialization=doctor["specialization"],
            )
            user.is_active = True
            user.save(update_fields=["is_active"])
        return user


class DoctorSerializer(serializers.ModelSerializer):
    specialization = SpecializationSerializer(read_only=True)
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = ["id", "user", "specialization", "address"]
        read_only_fields = ("specialization",)
