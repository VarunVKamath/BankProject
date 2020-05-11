from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
# Create your models here.

#Class to create User Table
class CustomerInfo(AbstractUser):
	
	Age = models.IntegerField(default=0)
	Address= models.CharField(max_length=20,default=0)
	AccountNumber=models.BigIntegerField(unique=True,default=0)
	Balance= models.BigIntegerField(default=0)
	Q1=models.CharField(max_length=20,default=0)
	Q2=models.CharField(max_length=20,default=0)
	Q3=models.CharField(max_length=20,default=0)
	#Photo=models.ImageField(upload_to='images/',default=None)

#Class to Create table to store approved Numbers for accounts.
class ApprovedAccNumbers(models.Model):
	AccountNumber=models.IntegerField(unique=True)






	







