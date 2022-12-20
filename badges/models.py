from django.db import models

# Create your models here.

class Badges(models.Model):
    name = models.CharField(null= False, max_length=200)
    experience = models.FloatField(null=False)
    photo = models.ImageField(null=False,blank=True, default='', upload_to='assets/resources/')
    