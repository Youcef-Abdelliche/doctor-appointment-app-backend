from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


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
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email


class Specialization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class UserProfile(models.Model):
    # SEX_CHOICES = (("M", "male"), ("F", "female"))
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    # phone_number = models.CharField(max_length=14)
    # image = models.ImageField()
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # sex = models.CharField(default="M", choices=SEX_CHOICES, max_length=1)

    # def __str__(self) -> str:
    #     return f"{self.first_name} {self.last_name}"
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Admin(UserProfile):
    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"


class Doctor(UserProfile):
    address = models.CharField(max_length=255)
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"


class Patient(UserProfile):
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"
