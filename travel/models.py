from django.db import models
from django.utils import timezone

class travel(models.Model):
    tid = models.BigAutoField(max_length=5,null=False,unique=True,primary_key=True)
    name = models.CharField(max_length=35,null=False)
    source = models.CharField(max_length=50,null=False)
    destination1 = models.CharField(max_length=500,null=False)
    destination2 = models.CharField(max_length=500,null=True,blank=True)
    destination3 = models.CharField(max_length=500,null=True,blank=True)
    destination4 = models.CharField(max_length=500,null=True,blank=True)
    distance = models.FloatField(null=False) 
    date = models.DateTimeField(blank=True,null=False)
    petrol_price = models.FloatField(null=False)   
    total_cost = models.FloatField(null=False)
    bill = models.ImageField(upload_to='bill/',null=True)


class distance(models.Model):
    tid = models.BigAutoField(max_length=5,null=False,unique=True,primary_key=True)
    address = models.CharField(max_length=50,null=True,unique=True) 
    latitude = models.DecimalField(max_digits=10, decimal_places=6,null=True) 
    longitude = models.DecimalField(max_digits=10, decimal_places=6,null=True) 

class petrol(models.Model):
    tid = models.BigAutoField(max_length=5,null=False,unique=True,primary_key=True)
    state = models.CharField(max_length=50,null=False,unique=True)
    petrol_price = models.FloatField(null=False) 