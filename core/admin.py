from django.contrib import admin

from .models import Admin, Doctor, Patient, Specialization, User

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
# admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Specialization)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("user", "address", "specialization")
