from django.contrib import admin

from .models import Admin, Doctor, Patient, Specialization, User, UserProfile

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Admin)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Specialization)
