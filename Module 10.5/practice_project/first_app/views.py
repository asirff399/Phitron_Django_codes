from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def first(request):
    d = {'v1':4,
         'v2':f"I'am Asir",
         'v3':'asir',
         'v4': datetime.datetime.now(),
         'v5':"",
         'v6':[
                {'name': 'zed', 'age': 19},
                {'name': 'amy', 'age': 22},
                {'name': 'joe', 'age': 31},
            ],
         'v7':24,
         'v8':11243412545,
         'v9':['a','b','c'],
         'v10':"My Name Is Asir",
         'v11':'my FIRST post',
         'v12': ['python', 'is', 'fun'],
        
         }
    return render(request,'first_app/first.html',d)

def home(request):
    return render(request,'first_app/home.html')

def product(request):
    return render(request,'first_app/product.html')

def about(request):
    return render(request,'first_app/about.html')

def contact(request):
    return render(request,'first_app/contact.html')