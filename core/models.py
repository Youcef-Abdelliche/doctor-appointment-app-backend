from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    USER_TYPE_CHOICES = ((1, "admin"), (2, "doctor"), (3, "patient"))
    SEX_CHOICES = (("M", "male"), ("F", "female"))

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=2)
    username = None
    email = models.EmailField(_("email address"), unique=True)
    sex = models.CharField(default=SEX_CHOICES[0][1], choices=SEX_CHOICES, max_length=1)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Specialization(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Admin(UserProfile):
    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"


class Doctor(UserProfile):
    address = models.CharField(max_length=255, blank=True)
    specialization = models.ForeignKey(
        Specialization, null=True, blank=True, on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"


class Patient(UserProfile):
    address = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"
