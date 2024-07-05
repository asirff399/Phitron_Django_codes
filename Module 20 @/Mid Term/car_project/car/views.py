from django.shortcuts import render,redirect
from django.views.generic import CreateView,DeleteView,UpdateView,DetailView
from . import models
from . import forms
from django.urls import reverse_lazy
from django.contrib import messages
from car.models import Order,Cars
# Create your views here.
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class AddCar(CreateView):
    model = models.Cars
    form_class = forms.CarForm
    template_name = 'add.html'
    success_url = reverse_lazy('add_car')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request,'Car added successfully.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request,'Car add failed.')
        return super().form_invalid(form)

@method_decorator(login_required, name='dispatch')
class UpdateCar(UpdateView):
    model = models.Cars
    form_class = forms.CarForm
    template_name = 'edit.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

@method_decorator(login_required, name='dispatch')
class DeleteCar(DeleteView):
    model = models.Cars
    pk_url_kwarg = 'id'
    template_name = 'delete.html'
    success_url = 'profile'

class CarDetailsView(DetailView):
    model = models.Cars
    template_name = 'details.html'
    pk_url_kwarg = 'id'

    def post(self,request,*args,**kwargs):
        comment_form = forms.CommentForm(data= self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request,*args,**kwargs)
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments= car.comments.all()
        comment_form = forms.CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context 

def CarOrder(request,id):
    car_instance = Cars.objects.get(pk=id)
    car = Cars.objects.all()
    if request.user.is_authenticated:
        if car_instance.quantity is not None and  car_instance.quantity > 0 :
            car_instance.quantity -= 1
            car_instance.save()
            Order.objects.create(user=request.user,car=car_instance)
            return redirect('profile') 
        else:
            return redirect('details',id=id)
    return render(request,'details.html')     

