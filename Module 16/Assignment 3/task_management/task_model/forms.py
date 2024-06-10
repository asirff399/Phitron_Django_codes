from django import forms
from task_model.models import TaskModel
class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
        labels = {
            'taskTitle':'Task Title',
            'taskDescription':'Task Description',
            'is_completed':'Is Completed',
            'taskAssignDate':'Task Assign Date',
        } 