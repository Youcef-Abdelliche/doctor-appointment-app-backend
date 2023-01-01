from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE_CHOICES = ((1, "admin"), (2, "doctor"), (3, "patient"))

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=2)


class Specialization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class UserProfile(models.Model):
    SEX_CHOICES = (("M", "male"), ("F", "female"))
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=14)
    # image
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(default="M", choices=SEX_CHOICES, max_length=1)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Admin(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user_profile.first_name} {self.user_profile.last_name}"


class Doctor(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT)
    address = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.user_profile.first_name} {self.user_profile.last_name}"


class Patient(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user_profile.first_name} {self.user_profile.last_name}"
