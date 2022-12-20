from django.db import models
from django.contrib.auth.models import User
from badges.models import Badges

# Create your models here.

class TablaProfile(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)
    url_image = models.ImageField(null=False,blank=True, default='', upload_to='assets/imgProfile/')
    id_badge = models.ForeignKey(Badges, on_delete=models.CASCADE,default=1)
    experience = models.FloatField(null=False)