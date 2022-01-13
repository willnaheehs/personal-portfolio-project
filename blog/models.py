from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateField(auto_now=True)
    url = models.URLField(blank=True) #by default blank=False, being true allows it to be blank