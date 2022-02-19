from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    describtion = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True)
    
# Create your models here.
