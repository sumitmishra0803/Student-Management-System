from django.db import models

# Create your models here.


class student(models.Model):
    name=models.CharField(max_length=30,null=True)
    rollnumber=models.CharField(max_length=30,null=True,)
    email=models.CharField(max_length=30,null=True)
    course=models.CharField(max_length=30,null=True)
    dob=models.CharField(max_length=30,null=True)
    phone=models.CharField(max_length=10,null=True)
    gender=models.CharField(max_length=30,null=True)
    address=models.CharField(max_length=30,null=True)
    tfee=models.CharField(max_length=30,null=True)
    pfee=models.CharField(max_length=30,null=True)
    lfee=models.CharField(max_length=30,null=True)
    image=models.FileField(null=True)
    
    
