from django.db import models

# Create your models here.

class users(models.Model):
    firstname= models.CharField(max_length=250)
    lastname= models.CharField(max_length=250)
    email= models.CharField(max_length=250)
    password= models.CharField(max_length=250)
    admin= models.BooleanField()
