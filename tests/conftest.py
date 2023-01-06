import pytest

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
