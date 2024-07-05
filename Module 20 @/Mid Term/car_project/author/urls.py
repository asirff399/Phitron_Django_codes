from django.urls import path,include
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.userLogout, name='logout'), 
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.editProfile, name='edit_profile'),
    path('profile/edit/pass_change/', views.passwordChange, name='pass_change'),
]