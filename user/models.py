from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TablaProfile(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)
    url_image = models.ImageField(null=False,blank=True, default='', upload_to='assets/imgProfile/')
    badges = models.CharField(max_length=1000,null=False)
    experience = models.FloatField(null=False)