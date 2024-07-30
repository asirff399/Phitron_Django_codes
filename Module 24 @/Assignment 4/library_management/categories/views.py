from django.forms import BaseModelForm
from django.shortcuts import render
from django.views.generic import ListView
from books.models import Books
from .models import CategoryModel
from .forms import CategoryForm
# Create your views here.

class CategoryView(ListView):
    model = CategoryModel 
    context_object_name = 'categories'
    template_name = './core/templates/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Books.objects.all()
        return context
