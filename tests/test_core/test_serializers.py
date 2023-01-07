import pytest

from core.serializers import DoctorSerializer, PatientSerializer


@pytest.mark.django_db
class TestPatientSerializer:
    def test_serialize_patient(self, patient):
        serializer = PatientSerializer(patient.patient)
        assert serializer.data

    def test_serialized_data(self, patient):
        profile = patient.patient
        valid_serialized_data = {
            "id": profile.pk,
            "user_id": profile.user_id,
            "address": profile.address,
            "date_of_birth": profile.date_of_birth,
        }

        serializer = PatientSerializer(data=valid_serialized_data)

        assert serializer.is_valid()
        assert serializer.errors == {}


@pytest.mark.django_db
class TestDoctorSerializer:
    def test_serialize_doctor(self, doctor):
        serializer = DoctorSerializer(doctor.doctor)
        assert serializer.data

    def test_serialized_data(self, doctor):
        profile = doctor.doctor
        profile.address = "Constantine"
        profile.specialization_id = 2
        valid_serialized_data = {
            "id": profile.pk,
            "user_id": profile.user_id,
            "address": profile.address,
            "specialization_id": profile.specialization_id,
        }

        serializer = DoctorSerializer(data=valid_serialized_data)

        assert serializer.is_valid()
        assert serializer.errors == {}
