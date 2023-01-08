from django.shortcuts import get_object_or_404
from rest_framework import serializers

from core.models import Doctor

from .models import Session


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
