from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


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
