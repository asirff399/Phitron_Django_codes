from django.db import models
from datetime import date
# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateField(default=date.today)

    def __str__(self):
        return self.taskTitle
 