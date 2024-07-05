from django.shortcuts import render,redirect
from task_category.forms import TaskCategoryForm
# Create your views here.
def taskCategory(request):
    if request.method == 'POST':
        form = TaskCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = TaskCategoryForm()
    return render(request,'category.html',{'form':form})