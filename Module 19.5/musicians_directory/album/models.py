from django.db import models
from datetime import date
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician,on_delete=models.CASCADE,default=None)
    release_date = models.DateField(default=date.today)
    number = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ]
    rating = models.CharField(max_length=10,choices=number,default=None)
    def __str__(self):
        return self.album_name  
