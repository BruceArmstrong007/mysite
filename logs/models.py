from django.db import models
from django.utils import timezone

# Create your models here.
class log(models.Model):
    tid = models.BigAutoField(null=False,unique=True,primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    log = models.IntegerField(null=True)
    fields = models.CharField(max_length=500,null=True,blank=True)
    href = models.CharField(max_length=500,null=False)
    go = models.CharField(max_length=500,null=False)