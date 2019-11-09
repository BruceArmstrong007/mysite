from django.db import models
from django.utils import timezone

# Create your models here.
class log(models.Model):
    tid = models.BigAutoField(max_length=5,null=False,unique=True,primary_key=True)
    section = models.CharField(max_length=10,null=False)
