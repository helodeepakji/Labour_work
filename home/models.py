from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
Education_Choices = [
    ('10th','10th'),
    ('12th','12th'),
    ('B','Graduate'),
    ('D','Post Graduate'),
    ('M','Phd'),
]

salary_type = [
    ('D_B','Daily Basis'),
    ('H_B','Hour Basis'),
]

gender_choices = [
    ('M','Male'),
    ('F','Female'),
    ('O','Other')
]
class Auth(AbstractUser):
    username = models.CharField(max_length=20,unique=True) #phone number
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10,choices=gender_choices,null=True,blank=True)
    Is_worker = models.BooleanField(default=False)
    Is_customer = models.BooleanField(default=False)
    first_name = None
    last_name = None
    email = None
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Customer(models.Model):
    Auth_ID = models.ForeignKey(Auth,on_delete=models.CASCADE)
    Email = models.EmailField(max_length=100,unique=True)

class Worker(models.Model):
    Auth_ID = models.ForeignKey(Auth,on_delete=models.CASCADE)
    Education = models.CharField(max_length=100,null=True,blank=True)
    Age = models.IntegerField()
    Profile_pic = models.ImageField(upload_to='profile_pic',null=True,blank=True)
    Category = models.CharField(max_length=100)
    Gov_id_type = models.CharField(max_length=100,default='Aadhar')
    Gov_id = models.CharField(max_length=20,null=True,blank=True)
    Salary_type = models.CharField(max_length=100,choices=salary_type)
    Salary = models.IntegerField(default=0,null=True,blank=True)
class Address(models.Model):
    WorkerID = models.ForeignKey(Worker,on_delete=models.CASCADE)
    Area = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Pincode = models.CharField(max_length=10)
    Default = models.BooleanField(default=False)

class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    Message = models.TextField()
    Email = models.EmailField(max_length=100,null=True,blank=True,default=None)