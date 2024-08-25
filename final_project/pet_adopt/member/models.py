from django.db import models
from .constants import MEMBER_TYPE_CHOICES
# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="customer/images/")
    type = models.CharField(max_length=30, choices=MEMBER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

