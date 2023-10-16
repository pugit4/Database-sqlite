from django.db import models

# Create your models here.
class leading(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=255)
    experiance = models.IntegerField()
    