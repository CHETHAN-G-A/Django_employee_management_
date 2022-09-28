from django.contrib import admin
from .models import Employee, Department, Role

# Register your models here.

admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Employee)
