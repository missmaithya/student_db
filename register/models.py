from django.db import models

# Create your models here.
class registration(models.Model):
    id=models.AutoField
    admin_no= models.CharField(max_length=4)

class student(models.Model):
    Full_name= models.CharField(max_length=30)
    reg_no= models.CharField(max_length=10,default='')
    email=models.EmailField(max_length=40)
    contact=models.IntegerField(default=15)
    registration=models.ForeignKey(registration,on_delete=models.CASCADE,default=10)
class hostel(models.Model):
    hostel_name= models.CharField(max_length=100)
    room_types= (('dormitory', 'Dormitory'),
        ('private', 'Private Room'),)
    room_type= models.CharField(max_length=20, choices=room_types)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    availability = models.BooleanField(default=True)
class hostel_allocation(models.Model):
    hostel = models.ForeignKey(hostel, on_delete=models.CASCADE)
    student_name = models.ForeignKey(student, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()


