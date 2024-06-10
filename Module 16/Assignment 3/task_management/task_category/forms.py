from django import forms
from task_category.models import TaskCategory
class TaskCategoryForm(forms.ModelForm):
    class Meta:
        model = TaskCategory
        fields = '__all__'
        labels = {
            'categoryName':'Category Name',
            'task':'Task',
        }