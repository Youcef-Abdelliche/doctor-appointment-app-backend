import pytest

# from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from core.models import Doctor, Specialization
from core.serializers import DoctorSerializer, UpdateDoctorSerializer

client = APIClient()


@pytest.mark.django_db
def test_list_doctor(api_client, doctor):
    count = Doctor.objects.all().count()
    # headers = {"HTTP_AUTHORIZATION": f"JWT {Token.key}"}
    response = api_client.get("/core/doctors/")

    assert response.status_code == 200
    assert count == 1


@pytest.mark.django_db
def test_rerieve_doctor(doctor):
    doctor = doctor.doctor
    expected_data = DoctorSerializer(doctor).data
    response = client.get(f"/core/doctors/{doctor.pk}/")

    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_update_doctor(doctor):
    doctor = doctor.doctor

    address = "Constantine, Algeria"
    specialization = Specialization.objects.create(name="Test")

    doctor.address = address
    doctor.specialization = specialization

    expected_data = UpdateDoctorSerializer(doctor).data
    response = client.patch(
        f"/core/doctors/{doctor.pk}/",
        dict(address=address, specialization_id=specialization.id),
    )

    assert response.status_code == 200
    assert response.data == expected_data
