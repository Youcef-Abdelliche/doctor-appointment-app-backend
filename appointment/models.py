from django.conf import settings
from django.db import models


class Session(models.Model):
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(unique=True)
    starts_at = models.TimeField()
    ends_at = models.TimeField()
