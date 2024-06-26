from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if not request.user.is_authenticated  :
        if request.method == 'POST':
            form = forms.RegistartionForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Account created successfully')
                redirect('login')
        else:
            form = forms.RegistartionForm()
        return render(request,'register.html',{'form':form,'type':'Register'})
    else:
        return redirect('login')
    
def change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'Password changed successfully')
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'register.html',{'form':form,'type':'Change Your password'})
    else:
        return redirect('login')

def change_pass2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'Password changed successfully')
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request,'register.html',{'form':form,'type':'Change Your Password'})
    else:
        return redirect('login')
    
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request,request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username=user_name,password=user_pass)
                if user is not None:
                    messages.success(request,'Logged in successfully')
                    login(request,user) 
                    return redirect('profile')
                else:
                    messages.warning(request,'Login information incorrect')
                    redirect('register')
        else:
            form = AuthenticationForm()
        return render(request,'register.html',{'form':form,'type':'Login'})
    else:
        return redirect('profile')
    
def user_logout(request):
    logout(request)
    messages.success(request,'Logged out successfully')
    return redirect('homepage')

@login_required 
def profile(request):
    if request.user.is_authenticated:
        user=request.user
        return render(request,'profile.html',{'user':user})
    else:
        return redirect('login')