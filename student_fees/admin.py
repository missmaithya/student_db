from django.contrib import admin
from student_fees.models import feeBalance,feePayments
# Register your models here.
admin.site.register(feeBalance)
admin.site.register(feePayments)