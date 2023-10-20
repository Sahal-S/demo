from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class employe(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255) 
    company=models.CharField(max_length=255)
    email=models.CharField(max_length=255,default='not@applicable')
    gender=models.CharField(max_length=255,default='prefer not to say')
    designation=models.TextField(max_length=255,default="Developer")
    DOB=models.DateTimeField(default="0000-00-00")
    interest=models.IntegerField(default=0)
    status=models.CharField(max_length=255,default='No actions')
    selected=ArrayField(models.CharField(max_length=100), blank=True, default=list)
    accepted=ArrayField(models.CharField(max_length=100), blank=True, default=list)
    rejected=ArrayField(models.CharField(max_length=100), blank=True, default=list)
    







    

