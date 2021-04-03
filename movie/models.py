from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    date_released = models.DateField()


    def __str__(self):
        return self.title
