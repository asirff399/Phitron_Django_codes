from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register,name='register'),
    # path('login/', views.user_login,name='login'),
    path('login/', views.UserLoginView.as_view() ,name='login'), 
    path('profile/', views.profile,name='profile'),
    path('profile/edit/', views.edit_profile,name='edit_profile'),
    path('profile/edit/pass_change/', views.pass_change,name='pass_change'),
    path('logout/', views.user_logout,name='logout'),
    # path('logout/', LogoutView.as_view() ,name='logout'), 
]     