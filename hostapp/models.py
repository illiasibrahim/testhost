from django.db import models

# Create your models here.


class Random(models.Model):
    image = models.ImageField(upload_to = 'pics')
    name = models.CharField(max_length=10,blank=True)