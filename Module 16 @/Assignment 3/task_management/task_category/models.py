from django.db import models
from datetime import date
from task_model.models import TaskModel
# Create your models here.
class TaskCategory(models.Model):
    categoryName = models.CharField(max_length=100)
    task = models.ManyToManyField(TaskModel,related_name='categories')

    def __str__(self):
        return self.categoryName
