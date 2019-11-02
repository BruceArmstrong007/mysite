from django.db import models
from django.utils import timezone

class user(models.Model):
        tid = models.BigAutoField(max_length=5,null=False,unique=True,primary_key=True)
        name = models.CharField(max_length=35,null=False)
        phone = models.IntegerField(unique=True,null=False)
        address = models.CharField(unique=True,max_length=500,null=False)
        designation = models.CharField(max_length=50,null=False)
        bloodgroup = models.CharField(max_length=5,null=False)
        dateofjoining = models.DateTimeField(blank=True,null=False)
        status = models.CharField(max_length=10,null=False)