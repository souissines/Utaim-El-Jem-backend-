from django.db import models

# Create your models here.
def upload_path(instance, filname):
    return '/'.join(['photos', str(instance.title), filname])

class Activity(models.Model):

    title= models.CharField(max_length=255, blank=False)
    activity_photo = models.ImageField(null=True,blank=True,upload_to=upload_path)

