import pytest

from appointment.serializers import AppointmentSerializer, SessionSerializer


@pytest.mark.django_db
class TestSessionSerializer:
    def test_serialize_data(self, session):
        serializer = SessionSerializer(session)
        assert serializer.data

    def test_serialized_data(self, session):
        valid_serialized_data = {
            "doctor_id": session.doctor_id,
            "date": session.date,
            "starts_at": session.starts_at,
            "ends_at": session.ends_at,
        }
        serializer = SessionSerializer(data=valid_serialized_data)
        assert serializer.is_valid()
        assert serializer.errors == {}


@pytest.mark.django_db
class TestAppointmentSerializer:
    def test_serialize_data(self, appointment):
        serializer = AppointmentSerializer(appointment)
        assert serializer.data

    def test_serialized_data(self, appointment):
        valid_serialized_data = {
            "session_id": appointment.session_id,
            "patient_id": appointment.patient_id,
            "starts_at": appointment.starts_at,
            "ends_at": appointment.ends_at,
        }
        serializer = AppointmentSerializer(data=valid_serialized_data)
        assert serializer.is_valid()
        assert serializer.errors == {}
