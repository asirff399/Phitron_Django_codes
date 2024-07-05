from django.shortcuts import render,redirect
from task_model.models import TaskModel
from task_model.forms import TaskModelForm
# Create your views here.
def taskModel(request):
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = TaskModelForm()
    return render(request,'task.html',{'form':form})

def Edit(request,id):
    task = TaskModel.objects.get(pk=id)
    form = TaskModelForm(instance=task)
    if request.method == 'POST':
        form = TaskModelForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = TaskModelForm()
    return render(request,'task.html',{'form':form})

def delete(request,id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('homepage') 