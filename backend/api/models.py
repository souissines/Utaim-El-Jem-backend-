from django.db import models

# Create your models here.

class Box(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=256)
    phone = models.IntegerField()
    message = models.CharField(max_length=256)