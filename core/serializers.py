# from django.db import transaction
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers

from .models import Doctor, Patient, Specialization, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "sex", "first_name", "last_name"]


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
        extra_kwargs = {
            "password": {"write_only": True},
        }

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


# class UserDoctorRegistrationSerializer(serializers.ModelSerializer):
#     doctor = CreateUpdateDoctorSerializer()

#     class Meta:
#         model = User
#         fields = [
#             "email",
#             "password",
#             "sex",
#             "first_name",
#             "last_name",
#             "user_type",
#             "doctor",
#         ]
#         extra_kwargs = {
#             "password": {"write_only": True},
#             "user_type": {"read_only": True},
#         }

#     def create(self, validated_data):
#         with transaction.atomic():
#             validated_data["user_type"] = 2
#             doctor = validated_data.pop("doctor")
#             user = User.objects.create_user(**validated_data)
#             Doctor.objects.create(
#                 user=user,
#                 address=doctor["address"],
#                 specialization=doctor["specialization"],
#             )
#             user.is_active = True
#             user.save(update_fields=["is_active"])
#         return user


class DoctorSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    specialization_id = serializers.IntegerField()

    class Meta:
        model = Doctor
        fields = ["id", "user_id", "specialization_id", "address"]


class UpdateDoctorSerializer(serializers.ModelSerializer):
    specialization_id = serializers.IntegerField()
    user_id = serializers.ReadOnlyField()

    class Meta:
        model = Doctor
        fields = ["id", "user_id", "specialization_id", "address"]


class PatientSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()

    class Meta:
        model = Patient
        fields = ["id", "user_id", "address", "date_of_birth"]


class UpdatePatientSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField()

    class Meta:
        model = Patient
        fields = ["user_id", "address", "date_of_birth"]
