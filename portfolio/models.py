from django.db import models
from django.db.models.fields import URLField

# Create your models here.
#inherits from django models class
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True) #by default blank=False, being true allows it to be blank

    def __str__(self):
        return self.title