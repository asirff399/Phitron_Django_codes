from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    type = {
        'STRING':'String',
        'WIND':'Wind',
        'PERCUSSION':'Percussion',
    }
    instrument_type = models.CharField(max_length=100,choices=type,default=None)

    def __str__(self): 
        return self.first_name
   
 