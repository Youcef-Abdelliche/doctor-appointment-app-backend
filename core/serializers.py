from django.db import transaction
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers

from .models import Doctor, Patient, Specialization, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "sex", "first_name", "last_name"]


class CreateUpdateDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["specialization", "address"]


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "sex",
            "first_name",
            "last_name",
            "user_type",
        ]
        # extra_kwargs = {
        #     "password": {"write_only": True},
        # }

    # def create(self, validated_data):
    #     with transaction.atomic():
    #         user = User.objects.create_user(**validated_data)
    #         user.is_active = True
    #         user.save(update_fields=["is_active"])
    #     return user

    # def perform_create(self, validated_data):
    #     with transaction.atomic():
    #         user = User.objects.create_user(**validated_data)
    #         user.is_active = True
    #         user.save(update_fields=["is_active"])
    #     return user


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
    user_id = serializers.CharField()
    specialization_id = serializers.CharField()

    class Meta:
        model = Doctor
        fields = ["id", "user_id", "specialization_id", "address"]


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = ["id", "user", "address", "date_of_birth"]


class CreateUpdatePatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["date_of_birth", "address"]


class UserPatientRegisrationSerializer(serializers.ModelSerializer):
    patient = CreateUpdatePatientSerializer()

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "sex",
            "first_name",
            "last_name",
            "user_type",
            "patient",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "user_type": {"read_only": True},
        }

    def create(self, validated_data):
        with transaction.atomic():
            validated_data["user_type"] = 3
            patient = validated_data.pop("patient")
            user = User.objects.create_user(is_active=True, **validated_data)
            Patient.objects.create(
                user=user,
                address=patient["address"],
                date_of_birth=patient["date_of_birth"],
            )
            # user.is_active = True
            # user.save(update_fields=["is_active"])
            # user.save()
        return user
