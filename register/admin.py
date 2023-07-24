from django.contrib import admin
from .models import registration,student,hostel,hostel_allocation
# Register your models here.
admin.site.register(registration)
admin.site.register(student)
admin.site.register(hostel)
admin.site.register(hostel_allocation)