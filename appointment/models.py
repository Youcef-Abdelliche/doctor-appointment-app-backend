from django.conf import settings
from django.db import models


class Session(models.Model):
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    starts_at = models.TimeField()
    ends_at = models.TimeField()


class Appointment(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    starts_at = models.TimeField()
    ends_at = models.TimeField()
    description = models.TextField(null=True, blank=True)
    # is_valid = models.BooleanField(default=False)
