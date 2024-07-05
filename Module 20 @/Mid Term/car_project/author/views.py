
from django.contrib.auth import logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render,redirect
from . import forms
from car.models import Order
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account created successfully.')
            return redirect('login')
    else:
        register_form = forms.RegisterForm()
        return render(request,'register.html',{'form': register_form})


class UserLogin(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self, form):
        messages.success(self.request,'Logged in successfully.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request,'Logged in failed.')
        return super().form_invalid(form)
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']='Login'
        return context
    
@login_required   
def profile(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)
        context = {
            'orders':orders,
        }
        return render(request,'profile.html',context)
    else:
        return redirect('login')
    # return render(request,'profile.html')

@login_required
def editProfile(request):
    if request.method == 'POST':
        form = forms.ChangeUserForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile updated successfully.')
            return redirect('profile')
    else:
        form = forms.ChangeUserForm(instance=request.user)
        return render(request,'edit_profile.html',{'form': form})

@login_required
def passwordChange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password updated successfully.')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'pass_change.html',{'form':form})

@login_required
def userLogout(request):
    logout(request)
    return redirect('login')