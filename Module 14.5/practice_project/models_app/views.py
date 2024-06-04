from django.shortcuts import render
from models_app.forms import TestModel
# Create your views here.
def model(request):
    if request.method == 'POST':
        form = TestModel(request.POST)
        if form.is_valid():
            form = TestModel()
    else:
        form = TestModel()
    return render(request,'models.html',{'form':form})

  