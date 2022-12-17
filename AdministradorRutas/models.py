from django.db import models

# Create your models here.

class Rutas(models.Model):
    shortname = models.CharField(max_length=100)
    fullname = models.TextField(blank=True)
    services = models.CharField(max_length=100)
    schedule = models.IntegerField(null=False)
    importantPlaces = models.TextField(blank=True)
    validate = models.CharField(max_length=100)
    score = models.IntegerField(null=True)