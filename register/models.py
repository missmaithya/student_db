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


