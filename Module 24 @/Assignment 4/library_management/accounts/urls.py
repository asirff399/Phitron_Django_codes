from django.urls import path,include
from .views import UserRegistrationView,UserLoginView,UserLogoutView,UserProfileUpdateView,UserProfile,passwordChange

urlpatterns = [
    path('signup/', UserRegistrationView.as_view(),name='signup'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('logout/', UserLogoutView,name='logout'),
    path('profile/',UserProfile,name='profile'), 
    path('profile/update_profile/', UserProfileUpdateView.as_view(),name='update_profile'),
    path('profile/update_profile/change_pass', passwordChange,name='change_pass'),
]
 