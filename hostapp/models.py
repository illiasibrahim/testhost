from django.db import models

# Create your models here.


class Random(models.Model):
    image = models.ImageField(upload_to = 'pics')