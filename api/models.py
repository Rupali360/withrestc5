from django.db import models

# Create your models here.
class Employees(models.Model):
    ename = models.CharField(max_length=60)
    esal = models.FloatField()
    eaddr =models.CharField(max_length=60)
    designation = models.CharField(max_length=255)
