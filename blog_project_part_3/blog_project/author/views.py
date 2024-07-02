from typing import Any
from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy

# Create your views here.
def register(request): 
    if request.method == 'POST': 
        register_forms = forms.RegistrationForm(request.POST)
        if register_forms.is_valid():
            register_forms.save()
            messages.success(request,'Account Created Successfully')
            return redirect('register')
    else: 
        register_forms = forms.RegistrationForm()
    return render(request,'register.html',{'form':register_forms, 'type':'Register'})  
 
def user_login(request): 
    if request.method == 'POST':
        login_forms = AuthenticationForm(request,request.POST)
        if login_forms.is_valid():
            user_name = login_forms.cleaned_data['username']
            user_pass = login_forms.cleaned_data['password']
            user = authenticate(username = user_name,password = user_pass)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in Successfully')
                return redirect('homepage')
            else:  
                messages.warning(request,'Login information incorrect')
                return redirect('register')
    else: 
        login_forms = AuthenticationForm()
    return render(request,'register.html',{'form':login_forms, 'type':'Login'})   

class UserLoginView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile')

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request,'Logged in successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request,'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

@login_required
def profile(request): 
    data = Post.objects.filter(author = request.user)
    return render(request,'profile.html',{'data':data})


@login_required
def edit_profile(request):
    if request.method == 'POST': 
        profile_forms = forms.ChangeUserForm(request.POST, instance= request.user)
        if profile_forms.is_valid():
            profile_forms.save()
            messages.success(request,'Profile Updated Successfully')
            return redirect('register')
    else: 
        profile_forms = forms.ChangeUserForm(instance= request.user) 
    return render(request,'update_profile.html',{'form':profile_forms, 'type':'Profile'})  


def pass_change(request):
    if request.method == 'POST': 
        form = PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Updated Successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else: 
        form = PasswordChangeForm(user= request.user) 
    return render(request,'pass_change.html',{'form':form})  


def user_logout(request):
    logout(request)
    return redirect('login')

