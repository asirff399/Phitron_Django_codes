from django.shortcuts import render
from django.views.generic import ListView
from books.models import Books
from categories.models import CategoryModel
# Create your views here.

class HomeView(ListView):
    model = CategoryModel 
    context_object_name = 'categories'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Books.objects.all()
        return context