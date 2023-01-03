from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Doctor, Patient, User


@receiver(post_save, sender=User)
def create_user_profile(sender, **kwargs):
    if kwargs["created"]:
        user = kwargs["instance"]
        if user.user_type == 2:
            Doctor.objects.create(user=user)
        else:
            Patient.objects.create(user=user)
