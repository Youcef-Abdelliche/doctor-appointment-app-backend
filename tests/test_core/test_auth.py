import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_login_user(doctor):
    response = client.post(
        "/auth/jwt/create/", dict(email="doctor@example.com", password="doctor141998")
    )

    assert response.status_code == 200


@pytest.mark.django_db
def test_login_user_fail():
    response = client.post(
        "/auth/jwt/create/", dict(email="test@example.com", password="test14199")
    )

    assert response.status_code == 401
