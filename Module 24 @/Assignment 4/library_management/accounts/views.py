from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login,logout
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserUpdateForm
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from books.models import Order
# Create your views here.
class UserRegistrationView(FormView):
    template_name = 'user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name = 'user_login.html'

    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    
@login_required   
def UserProfile(request):
    if request.user.is_authenticated:
        user_account = request.user.account
        orders = Order.objects.filter(account=user_account) 
        context = {
            'orders':orders,
        }
        return render(request,'profile.html',context)
    else:
        return redirect('login')
    # return render(request,'profile.html')
    
class UserProfileUpdateView(View):
    template_name = 'update_profile.html'

    def get(self,request):
        form = UserUpdateForm(instance=request.user)
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form = UserUpdateForm(request.Post,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request,self.template_name,{'form':form})