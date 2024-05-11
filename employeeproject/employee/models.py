from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Company(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=100)
    address=models.TextField()

    def __str__(self):
        return self.name

class Department(models.Model):
    id=models.IntegerField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Employee(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    image=models.ImageField(upload_to='employee/images',blank=True,null=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    address=models.TextField()
    phone_number=models.IntegerField()
    salary=models.IntegerField()
    joined_date=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    phone=models.IntegerField(default=0)
    address=models.TextField(default="")


    def __str__(self):
        return self.username