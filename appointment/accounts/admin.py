from django.contrib import admin
from .models import Doctor,patient,Staff

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Staff)
admin.site.register(patient)