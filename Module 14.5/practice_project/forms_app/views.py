from django.shortcuts import render
from forms_app.forms import testform
# Create your views here.
def myForm(request):
    if request.method == 'POST':
        form = testform(request.POST)
        if form.is_valid(): 
            form = testform()
    else:
        form = testform()
    return render(request,'forms.html',{'form':form}) 