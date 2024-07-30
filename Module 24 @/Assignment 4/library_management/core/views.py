from django.shortcuts import render
from books.models import Books
from categories.models import CategoryModel
# Create your views here.

def Home(request,category_slug=None):
    data = Books.objects.all()
    if category_slug is not None:
        category = CategoryModel.objects.get(slug = category_slug)
        data = Books.objects.filter(category=category)
    category = CategoryModel.objects.all()
    return render(request,'index.html',{'data':data,'categories':category})