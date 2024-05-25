from django.shortcuts import render
import datetime
# Create your views here.
def home (request):
    d = {'author':'rohim','age': 9,'lst':['Python','is','best'],'birthday':datetime.datetime.now(),'val':" ",'courses':[
        {
            'id':1,
            'name':'Python',
            'fee' : 5000,
        },
        {
            'id':2,
            'name':'Django',
            'fee' : 10000,
        },
        {
            'id' : 2,
            'name' :'C/C++',
            'fee' : 2000,
        }

        ]}
    return render(request,'home.html',d)