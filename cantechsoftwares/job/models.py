from datetime import datetime
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

user_type =['Applicant','Recruiter','Admin']

class UserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uname = models.CharField(max_length=100, blank=True, null=True) 
    uphone = models.CharField(max_length=13, blank=True, null=True,) 
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10,null=True,blank=True)
    uemail = models.EmailField(unique=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100,null=True, blank=True)
    date_created = models.DateTimeField(default=datetime.now())
    domain = models.CharField(max_length=100,null=True,blank=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    total_projects = models.IntegerField(default=0)
    age = models.IntegerField(default=0,null=True,blank=True)
    experience = models.IntegerField(default=0,null=True,blank=True)
    type = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100)
    freelance = models.BooleanField(default=False)
    aboutu = models.TextField(max_length=2000,null=True,blank=True)
    user_type = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.user.username

class RecruiterModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rname = models.CharField(max_length=100, blank=True, null=True) 
    rphone = models.CharField(max_length=13, blank=True, null=True,) 
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100,null=True,blank=True)
    company = models.CharField(max_length=100,null=True,blank=True)
    remail = models.EmailField(unique=True)
    status = models.CharField(max_length=100,null=True,blank=True,default='Pending')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    user_type = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.user.username

    
    
