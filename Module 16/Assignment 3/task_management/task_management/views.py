from django.shortcuts import render
from task_model.models import TaskModel

def home(request):
    data = TaskModel.objects.prefetch_related('categories').all()
    return render(request,'home.html',{'data':data}) 
 
def show(request):
    data = TaskModel.objects.prefetch_related('categories').all()
    return render(request,'show.html',{'data':data})  