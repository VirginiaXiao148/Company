from django.contrib import admin
from .models import Employee, Shift, Leave

# Register your models here.
admin.site.register(Employee)
admin.site.register(Shift)
admin.site.register(Leave)