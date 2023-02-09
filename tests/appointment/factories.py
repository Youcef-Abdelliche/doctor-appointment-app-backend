import factory

from appointment.models import Session

# from faker import Faker
# from pytest_factoryboy import register


class SessionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Session
