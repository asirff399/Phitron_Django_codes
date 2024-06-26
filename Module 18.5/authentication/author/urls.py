
from django.urls import path,include
from . import views

urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/change_pass/with/',views.change_pass,name='change_pass_with'),
    path('profile/change_pass/without/',views.change_pass2,name='change_pass_without'),
    path('register/',views.register,name='register'),
] 
