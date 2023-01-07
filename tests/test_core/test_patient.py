from datetime import date

import pytest
from rest_framework.test import APIClient

from core.models import Patient
from core.serializers import PatientSerializer, UpdatePatientSerializer

client = APIClient()


@pytest.mark.django_db
def test_list_patient(patient):
    count = Patient.objects.all().count()
    response = client.get("/core/patients/")

    assert response.status_code == 200
    assert count == 1


@pytest.mark.django_db
def test_rerieve_patient(patient):
    patient = patient.patient
    expected_data = PatientSerializer(patient).data
    response = client.get(f"/core/patients/{patient.pk}/")

    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_update_patient(patient):
    patient = patient.patient

    address = "Constantine, Algeria"
    date_of_birth = date(1998, 8, 14)

    patient.address = address
    patient.date_of_birth = date_of_birth

    expected_data = UpdatePatientSerializer(patient).data
    response = client.patch(
        f"/core/patients/{patient.pk}/",
        dict(address=address, date_of_birth=date_of_birth),
    )

    assert response.status_code == 200
    assert response.data == expected_data
