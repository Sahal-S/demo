from django.db import models

# Create your models here.


class employe(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    company=models.CharField(max_length=255)
    email=models.CharField(max_length=255,default='not@applicable')
    gender=models.CharField(max_length=255,default='prefer not to say')
    designation=models.TextField(max_length=255,default="Developer")
    DOB=models.DateTimeField(default="0000-00-00")







    

