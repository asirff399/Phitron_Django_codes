from django.db import models
from django.utils.text import slugify
# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)

    def __str__(self):
        return self.name