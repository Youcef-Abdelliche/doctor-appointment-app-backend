from django.shortcuts import get_object_or_404
from rest_framework import serializers

from core.models import Doctor

from .models import Appointment, Session


class SessionSerializer(serializers.ModelSerializer):

    doctor_id = serializers.IntegerField()

    class Meta:
        model = Session
        fields = ["id", "doctor_id", "date", "starts_at", "ends_at"]

    def create(self, validated_data):
        user_id = validated_data.pop("doctor_id")
        doctor = get_object_or_404(Doctor.objects.all(), user_id=user_id)
        session = Session.objects.create(doctor_id=doctor.user_id, **validated_data)
        return session


class UpdateSessionSerializer(serializers.ModelSerializer):
    doctor_id = serializers.ReadOnlyField()

    class Meta:
        model = Session
        fields = ["doctor_id", "date", "starts_at", "ends_at"]


class AppointmentSerializer(serializers.ModelSerializer):
    session_id = serializers.IntegerField()
    patient_id = serializers.ReadOnlyField()

    class Meta:
        model = Appointment
        fields = [
            "id",
            "session_id",
            "patient_id",
            "starts_at",
            "ends_at",
            "description",
        ]

    def create(self, validated_data):
        # user_id = validated_data.pop("patient_id")
        user_id = self.context["user_id"]
        session_id = validated_data.pop("session_id")
        # patient = get_object_or_404(Patient.objects.all(), user_id=user_id)
        session = get_object_or_404(Session.objects.all(), pk=session_id)
        appointment = Appointment.objects.create(
            patient_id=user_id, session_id=session.pk, **validated_data
        )
        return appointment


class UpdateAppointmentSerializer(serializers.ModelSerializer):
    session_id = serializers.ReadOnlyField()

    class Meta:
        model = Appointment
        fields = ["session_id", "starts_at", "ends_at", "description"]


class SessionAppointmentSerializer(serializers.ModelSerializer):
    appointment_set = AppointmentSerializer(many=True)

    class Meta:
        model = Session
        fields = ["id", "doctor", "date", "starts_at", "ends_at", "appointment_set"]
