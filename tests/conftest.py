from datetime import date, time

import pytest

from appointment.models import Appointment, Session
from core.models import User


@pytest.fixture
def doctor():
    user = User.objects.create_user(
        email="doctor@example.com",
        password="doctor141998",
        first_name="test",
        last_name="test",
        sex="M",
        user_type=2,
    )
    return user


@pytest.fixture
def patient():
    user = User.objects.create_user(
        email="patient@example.com",
        password="patient141998",
        first_name="test",
        last_name="test",
        sex="M",
        user_type=3,
    )
    return user


@pytest.fixture
def session(doctor):
    # user = User.objects.create_user(
    #     email="doctor@example.com",
    #     password="doctor141998",
    #     first_name="test",
    #     last_name="test",
    #     sex="M",
    #     user_type=2,
    # )
    user = doctor
    session = Session.objects.create(
        doctor=user,
        date=date(2020, 8, 3),
        starts_at=time(8, 8, 0),
        ends_at=time(8, 8, 0),
    )
    return session


@pytest.fixture
def appointment(session, patient):
    appointment = Appointment.objects.create(
        session=session,
        patient=patient,
        starts_at=time(8, 8, 0),
        ends_at=time(8, 8, 0),
    )
    return appointment
