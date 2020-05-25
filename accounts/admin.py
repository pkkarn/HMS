from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointments)
admin.site.register(Patient_Outstandings)
admin.site.register(Doctor_Outstandings)
admin.site.register(Prescription)

